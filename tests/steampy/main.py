from sys import path
path.append("../../") 

from steampy import Crawler

if __name__ == "__main__":
    crawler: Crawler = Crawler()

    response = crawler.reqUrl("https://store.steampowered.com/search/?specials=1")
    
    print(response)