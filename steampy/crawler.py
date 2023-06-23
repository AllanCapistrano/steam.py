from requests import get, Response
from bs4 import BeautifulSoup

class Crawler:
    def reqUrl(self, url: str) -> BeautifulSoup:
        """Buscar o conteúdo de uma página com base em uma URL.

        Parameters
        -----------
        url: :class:`str`
            Url do site.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """

        res: Response       = get(url)
        soup: BeautifulSoup = BeautifulSoup(res.text, 'lxml')

        return soup