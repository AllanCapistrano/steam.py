from typing import List, Tuple, Dict

from bs4 import BeautifulSoup

from .crawler import Crawler
from .utils import verify_amount
from .services import is_available_language, format_currency

class CrawlerNewReleases(Crawler):
    def get_games_titles(
        self, 
        url: str, 
        amount_games_titles: int = 50, 
        language: str = "english"
    ) -> List[str]:
        """ Return the games titles that are in 'New Releases' list.

        Parameters
        ----------
        url: :class:`str`
            New Releases URL.

        amount_games_titles: :class:`int`
            (Optional) The minimum number of game titles. The default is `50`.

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

        url                 = f"{url}?l={language}"
        soup: BeautifulSoup = self.reqUrl(url).find(
            "div", 
            id="tab_newreleases_content"
        )
        div_tags: BeautifulSoup = soup.find_all("div", class_="tab_item_name")

        for index in range(0, min(amount_games_titles, len(div_tags))):
            titles.append(div_tags[index].contents[0])

        return titles

    def get_games_discounts(
        self, 
        url: str, 
        amount_games_discounts: int = 50
    ) -> List[str | None]:
        """ Return the games discounts that are in 'New Releases' list.

        Parameters
        ----------
        url: :class:`str`
            New Releases URL.

        amount_games_discounts: :class:`int`
            (Optional) The minimum number of game discounts. The default is `50`.

        Returns
        -------
        :class:`List[str | None]`
        """

        discounts: List[str]        = []
        amount_games_discounts: int = verify_amount(amount_games_discounts)
        soup: BeautifulSoup = self.reqUrl(url).find(
            "div", 
            id="tab_newreleases_content"
        )
        div_tags: BeautifulSoup = soup.find_all(
            "div", 
            class_="tab_item_discount"
        )

        for index in range(0, min(amount_games_discounts, len(div_tags))):
            if("no_discount" in div_tags[index].get_attribute_list("class")):
                discounts.append(None)
            else:
                discount = div_tags[index].contents[0]
                discounts.append(discount.contents[0])

        return discounts

    def get_games_prices(
        self, 
        url: str, 
        amount_games_prices: int = 50,
        language: str = "english",
        currency: str = "USD"
    ) -> Tuple[List[str | None], List[str | None]]:
        """ Return the games old and discount prices that are in 'New Releases' 
        list.

        Parameters
        ----------
        url: :class:`str`
            New Releases URL.

        amount_games_prices: :class:`int`
            (Optional) The minimum number of games prices. The default is `50`.

        language: :class:`str`
            (Optional) Request language. The default is `english`.

        currency: :class:`str`
            (Optional) Request currency.

        Returns
        -------
        original_prices: :class:`List[str | None]`
        
        discount_prices: :class:`List[str | None]`
        """

        original_prices: List[str] = []
        discount_prices: List[str] = []
        amount_games_prices: int   = verify_amount(amount_games_prices)

        url                 = f"{url}?l={language}&cc={format_currency(currency)}"
        soup: BeautifulSoup = self.reqUrl(url).find(
            "div", 
            id="tab_newreleases_content"
        )
        div_tags: BeautifulSoup = soup.find_all(
            "div", 
            class_="tab_item_discount"
        )

        for index in range(0, min(amount_games_prices, len(div_tags))):
            prices_div = div_tags[index].contents[-1]
            
            if("no_discount" in div_tags[index].get_attribute_list("class")):
                discount_price = prices_div.contents[0]
                
                original_prices.append(None)
                discount_prices.append(discount_price.contents[0])
            else:
                original_price = prices_div.contents[0]
                discount_price = prices_div.contents[1]

                original_prices.append(original_price.contents[0])
                discount_prices.append(discount_price.contents[0])

        return original_prices, discount_prices
    
    def get_games_urls(
        self, 
        url: str, 
        amount_games_urls: int = 50
    ) -> List[str]:
        """ Returns the URLs of the games that are in 'New Releases' list.

        Parameters
        ----------
        url: :class:`str`
            New Releases URL.

        amount_games_urls: :class:`int`
            (Optional) The minimum number of games URLs. The default is `50`.

        Returns
        -------
        urls: :class:`List[str]`
        """

        urls: List[str]        = []
        amount_games_urls: int = verify_amount(amount_games_urls)

        soup: BeautifulSoup = self.reqUrl(url).find(
            "div", 
            id="tab_newreleases_content"
        )
        a_tags: BeautifulSoup = soup.find_all("a")

        for index in range(0, min(amount_games_urls, len(a_tags))):
            urls.append(a_tags[index].get_attribute_list("href")[0])

        urls.pop(-1) # Removing 'POPULAR NEW RELEASES' URL.

        return urls