from sys import path
path.append("../../") 

from steampy import Crawler, CrawlerSpecials

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/search/?specials=1"

    crawler: Crawler = CrawlerSpecials()

    gp1, gp2 = crawler.getGamesPrices(url)

    gt = crawler.getGamesTitles(url, language="brazilian")
    
    print(gt)
    print(gp2, len(gp2))