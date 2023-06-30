from sys import path
path.append("../../") 

from steampy import CrawlerSpecials

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/search/?specials=1"

    crawler: CrawlerSpecials = CrawlerSpecials()

    games_titles = crawler.get_games_titles(url, language="brazilian")
    print(games_titles, len(games_titles), "\n")

    games_discounts = crawler.get_games_discounts(url)
    print(games_discounts, len(games_discounts), "\n")

    games_prices = crawler.get_games_prices(url, currency="BRL")
    print(games_prices, len(games_prices), "\n")
    
    games_images = crawler.get_games_images(url, amount_games_images=3)
    print(games_images, len(games_images), "\n")
    
    games_urls = crawler.get_games_urls(url)
    print(games_urls, len(games_urls), "\n")