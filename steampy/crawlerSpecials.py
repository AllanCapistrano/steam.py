from typing import List

from bs4 import BeautifulSoup

from .crawler import Crawler

class CrawlerSpecials(Crawler):
    def getGamesTitles(self, url: str, amount_game_titles: int = 50) -> List[str]:
        """ Return the games titles that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_game_titles: :class:`int`
            The number of game titles. The default is `50`.

        Returns
        -------
        :class:`List[str]`
        """

        titles: List[str]       = []
        amount_game_titles: int = self.__verify_amount__(amount_game_titles)
        soup: BeautifulSoup     = self.reqUrl(url).find_all("span", class_="title")

        for index in range(0, amount_game_titles):
            titles.append(soup[index].contents[0])

        return titles

    def getGamesDiscounts(self, url: str, amount_game_discounts: int = 50) -> List[str | None]:
        """ Return the games discounts that are in 'Specials' list.

        Parameters
        ----------
        url: :class:`str`
            Specials URL.

        amount_game_discounts: :class:`int`
            The number of game discounts. The default is `50`.

        Returns
        -------
        :class:`List[str | None]`
        """

        discounts: List[str]       = []
        amount_game_discounts: int = self.__verify_amount__(amount_game_discounts)
        soup: BeautifulSoup        = self.reqUrl(url).find_all("div", class_="search_discount")

        for index in range(0, amount_game_discounts):
            if (len(soup[index].contents) == 3):
                discount = soup[index].contents[1]
                discounts.append(discount.contents[0])
            else:
                discounts.append(None)

        return discounts

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