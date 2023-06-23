from typing import List

from bs4 import BeautifulSoup

from .crawler import Crawler
from .utils import remove_extra_whitespace

class CrawlerSpecials(Crawler):
    def getGamesTitles(self, url: str, amount_games_titles: int = 50) -> List[str]:
        """ Return the games titles that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_titles: :class:`int`
            The number of game titles. The default is `50`.

        Returns
        -------
        :class:`List[str]`
        """

        titles: List[str]        = []
        amount_games_titles: int = self.__verify_amount__(amount_games_titles)
        soup: BeautifulSoup      = self.reqUrl(url).find_all("span", class_="title")

        for index in range(0, amount_games_titles):
            titles.append(soup[index].contents[0])

        return titles

    def getGamesDiscounts(self, url: str, amount_games_discounts: int = 50) -> List[str | None]:
        """ Return the games discounts that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_discounts: :class:`int`
            The number of game discounts. The default is `50`.

        Returns
        -------
        :class:`List[str | None]`
        """

        discounts: List[str]        = []
        amount_games_discounts: int = self.__verify_amount__(amount_games_discounts)
        soup: BeautifulSoup         = self.reqUrl(url).find_all("div", class_="search_discount")

        for index in range(0, amount_games_discounts):
            if (len(soup[index].contents) == 3):
                discount = soup[index].contents[1]
                discounts.append(discount.contents[0])
            else:
                discounts.append(None)

        return discounts

    def getGamesPrices(self, url: str, amount_games_prices: int = 50) -> (List[str | None], List[str | None]):
        """ Return the games old and discount prices that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_games_prices: :class:`int`
            The number of games prices. The default is `50`.

        Returns
        -------
        old_prices: :class:`List[str | None]`
        
        discount_prices: :class:`List[str | None]`
        """

        old_prices: List[str]      = []
        discount_prices: List[str] = []
        amount_games_prices: int   = self.__verify_amount__(amount_games_prices)
        soup: BeautifulSoup        = self.reqUrl(url).find_all("div", class_="search_price")

        for index in range(0, amount_games_prices):
            search_price_div: BeautifulSoup = soup[index].contents
            
            if (len(search_price_div) == 4):
                old_prices.append(search_price_div[1].contents[0].contents[0])
                discount_prices.append(remove_extra_whitespace(search_price_div[-1]))
            else:
                old_prices.append(None)
                discount_prices.append(None)

        return old_prices, discount_prices


    def __verify_amount__(self, amount) -> int:
        """ Check whether the amount parameter is valid or not.

        Parameters
        ----------
        amount: :class:`str`
            amount of something.
       

        Returns
        -------
        :class:`int`
        """
        
        if (amount > 50 or amount <= 0):
            amount = 50

        return amount