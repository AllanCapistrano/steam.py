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
