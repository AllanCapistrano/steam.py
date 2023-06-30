from typing import List, Dict, Tuple

from bs4 import BeautifulSoup

from .crawler import Crawler
from .utils import remove_extra_whitespace, verify_amount, sanitize_srcset
from .services import is_available_language, format_currency

class CrawlerSpecials(Crawler):
    def get_games_titles(
        self, 
        url: str, 
        amount_games_titles: int = 50, 
        language: str = "english"
    ) -> List[str]:
        """ Return the games titles that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_titles: :class:`int`
            (Optional) The number of game titles. The default is `50`.

        language: :class:`str`
            (Optional) Request language. The default is `english`.

        Returns
        -------
        :class:`List[str]`
        """

        titles: List[str]        = []
        amount_games_titles: int = verify_amount(amount_games_titles)

        if (not is_available_language(language)):
            language = "english"

        url                 = f"{url}&l={language}"
        soup: BeautifulSoup = self.reqUrl(url).find_all("span", class_="title")

        for index in range(0, amount_games_titles):
            titles.append(soup[index].contents[0])

        return titles

    def get_games_discounts(
        self, 
        url: str, 
        amount_games_discounts: int = 50
    ) -> List[str | None]:
        """ Return the games discounts that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_discounts: :class:`int`
            (Optional) The number of game discounts. The default is `50`.

        Returns
        -------
        :class:`List[str | None]`
        """

        discounts: List[str]        = []
        amount_games_discounts: int = verify_amount(
            amount_games_discounts
        )
        soup: BeautifulSoup = self.reqUrl(url).find_all(
            "div", 
            class_="search_discount"
        )

        for index in range(0, amount_games_discounts):
            if (len(soup[index].contents) == 3):
                discount = soup[index].contents[1]
                discounts.append(discount.contents[0])
            else:
                discounts.append(None)

        return discounts

    def get_games_prices(
        self, 
        url: str, 
        amount_games_prices: int = 50,
        currency: str = "USD"
    ) -> List[Dict[str, str]]:
        """ Return the games old and discount prices that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_prices: :class:`int`
            (Optional) The number of games prices. The default is `50`.

        currency: :class:`str`
            (Optional) Request currency.

        Returns
        -------
        games_prices: :class:`List[Dict[str, str]]`
        """

        games_prices: List[Dict[str, str]] = []
        amount_games_prices: int           = verify_amount(amount_games_prices)

        url                 = f"{url}&cc={format_currency(currency)}"
        soup: BeautifulSoup = self.reqUrl(url).find_all(
            "div", 
            class_="search_price"
        )

        for index in range(0, amount_games_prices):
            search_price_div: BeautifulSoup = soup[index].contents
            
            if (len(search_price_div) == 4):
                games_prices.append(
                    {
                        "original_price": 
                            search_price_div[1].contents[0].contents[0], 
                        "discount_price": remove_extra_whitespace(
                            search_price_div[-1]
                        )
                    }
                )
            else:
                games_prices.append(
                    {
                        "original_price": None,
                        "discount_price": None
                    }
                )

        return games_prices

    def get_games_images(
        self, 
        url: str, 
        amount_games_images: int = 50
    ) -> List[Dict[str, str]]:
        """ Returns the 1x and 2x images of the games that are in 'Specials' 
        list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_images: :class:`int`
            (Optional) The number of games images. The default is `50`.

        Returns
        -------
        images: :class:`List[Dict[str, str]]`
        """
        
        images: List[Dict[str, str]] = []
        amount_games_images: int     = verify_amount(amount_games_images)

        soup: BeautifulSoup = self.reqUrl(url).find_all(
            "div", 
            class_="search_capsule"
        )

        for index in range(0, amount_games_images):
            image_tag = soup[index].contents[0]
            srcset    = image_tag.get_attribute_list('srcset')[0]
            
            image_url_1x, image_url_2x = sanitize_srcset(srcset)
            images.append({"1x": image_url_1x, "2x": image_url_2x})    

        return images

    def get_games_urls(
        self, 
        url: str, 
        amount_games_urls: int = 50
    ) -> List[str]:
        """ Returns the URLs of the games that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_urls: :class:`int`
            (Optional) The number of games URLs. The default is `50`.

        Returns
        -------
        urls: :class:`List[str]`
        """

        urls: List[str]        = []
        amount_games_urls: int = verify_amount(amount_games_urls)

        soup: BeautifulSoup = self.reqUrl(url).find(
            "div", 
            id="search_resultsRows"
        )
        a_tags: BeautifulSoup = soup.find_all("a")

        for index in range(0, amount_games_urls):
            urls.append(a_tags[index].get_attribute_list("href")[0])
            
        return urls