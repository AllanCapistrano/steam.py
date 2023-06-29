from sys import path
path.append("../../") 

from steampy import CrawlerSpecials

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/search/?specials=1"

    crawler: CrawlerSpecials = CrawlerSpecials()

    # gt = crawler.get_games_titles(url, language="brazilian")
    # gp1, gp2 = crawler.get_games_prices(url, currency="CAD")
    # gi = crawler.get_games_images(url, amount_games_images=3)
    gu = crawler.get_games_urls(url)

    # print(gt, len(gt))
    # print(gp2, len(gp2))
    # print(gi)
    print(gu, len(gu))