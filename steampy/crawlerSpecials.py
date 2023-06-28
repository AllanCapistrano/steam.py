from typing import List

from bs4 import BeautifulSoup

from .crawler import Crawler
from .utils import remove_extra_whitespace, verify_amount
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
    ) -> (List[str | None], List[str | None]):
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
        original_prices: :class:`List[str | None]`
        
        discount_prices: :class:`List[str | None]`
        """

        original_prices: List[str] = []
        discount_prices: List[str] = []
        amount_games_prices: int   = verify_amount(amount_games_prices)

        url                 = f"{url}&cc={format_currency(currency)}"
        soup: BeautifulSoup = self.reqUrl(url).find_all(
                "div", 
                class_="search_price"
            )

        for index in range(0, amount_games_prices):
            search_price_div: BeautifulSoup = soup[index].contents
            
            if (len(search_price_div) == 4):
                original_prices.append(search_price_div[1].contents[0].contents[0])
                discount_prices.append(
                    remove_extra_whitespace(search_price_div[-1])
                )
            else:
                original_prices.append(None)
                discount_prices.append(None)

        return original_prices, discount_prices