from typing import List

from bs4 import BeautifulSoup

from .crawler import Crawler
from .utils import remove_extra_whitespace, verify_amount
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

        url                 = f"{url}?l={language}"
        soup: BeautifulSoup = self.reqUrl(url).find_all("div", class_="tab_item_name")

        for index in range(0, amount_games_titles):
            titles.append(soup[index].contents[0])

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
            class_="tab_item_discount"
        )

        for index in range(0, amount_games_discounts):
            if("no_discount" in soup[index].get_attribute_list("class")):
                discounts.append(None)
            else:
                discount = soup[index].contents[0]
                discounts.append(discount.contents[0])

        return discounts

    def get_games_prices(
        self, 
        url: str, 
        amount_games_prices: int = 50,
        language: str = "english",
        currency: str = "USD"
    ) -> (List[str | None], List[str | None]):
        """ Return the games old and discount prices that are in 'New Releases' 
        list.

        Parameters
        ----------
        url: :class:`str`
            New Releases URL.

        amount_games_prices: :class:`int`
            (Optional) The number of games prices. The default is `50`.

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
        soup: BeautifulSoup = self.reqUrl(url).find_all(
                "div", 
                class_="tab_item_discount"
            )

        for index in range(0, amount_games_prices):
            prices_div = soup[index].contents[-1]
            
            if("no_discount" in soup[index].get_attribute_list("class")):
                discount_price = prices_div.contents[0]
                
                original_prices.append(None)
                discount_prices.append(discount_price.contents[0])
            else:
                original_price = prices_div.contents[0]
                discount_price = prices_div.contents[1]

                original_prices.append(original_price.contents[0])
                discount_prices.append(discount_price.contents[0])

        return original_prices, discount_prices