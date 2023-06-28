from sys import path
path.append("../../") 

from steampy import CrawlerNewReleases

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/explore/new/"

    crawler: CrawlerNewReleases = CrawlerNewReleases()

    gp1, gp2 = crawler.get_games_prices(url)
    
    print(gp1)
    print()
    print(gp2)