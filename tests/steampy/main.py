from sys import path
path.append("../../") 

from steampy import Crawler, CrawlerSpecials

if __name__ == "__main__":
    crawler: Crawler = CrawlerSpecials()

    response = crawler.getGamesDiscounts("https://store.steampowered.com/search/?specials=1")
    
    print(response, len(response))