from requests import get, Response
from bs4 import BeautifulSoup

class Crawler:
    def reqUrl(self, url: str) -> BeautifulSoup:
        """Return the page content by the URL..
        

        Parameters
        -----------
        url: :class:`str`
            Website URL.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """

        res: Response       = get(url)
        soup: BeautifulSoup = BeautifulSoup(res.text, 'lxml')

        return soup