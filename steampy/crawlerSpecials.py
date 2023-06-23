from typing import List

from .crawler import Crawler

class CrawlerSpecials(Crawler):
    def getGamesTitles(self, url: str, amount_game_titles: int = 50) -> List[str]:
        """ Return the game titles that are in 'Specials' list.

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

        titles: List[str] = []

        if (amount_game_titles > 50 or amount_game_titles <= 0):
            amount_game_titles = 50

        for title in self.reqUrl(url).find_all("span", class_="title"):
            titles.append(title.contents[0])

        return titles[0: amount_game_titles]