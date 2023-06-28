from sys import path
path.append("../../") 

from steampy import CrawlerNewReleases

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/explore/new/"

    crawler: CrawlerNewReleases = CrawlerNewReleases()

    gt = crawler.get_games_discounts(url)
    
    print(gt)