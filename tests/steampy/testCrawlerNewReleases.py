from sys import path
path.append("../../") 

from steampy import CrawlerNewReleases

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/explore/new/"

    crawler: CrawlerNewReleases = CrawlerNewReleases()

    gt1, gt2 = crawler.get_games_prices(url)
    
    print(gt1)
    print()
    print(gt2)