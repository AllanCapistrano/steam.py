from sys import path
path.append("../../") 

from steampy import CrawlerNewReleases

if __name__ == "__main__":
    url: str = "https://store.steampowered.com/explore/new/"

    crawler: CrawlerNewReleases = CrawlerNewReleases()

    games_titles = crawler.get_games_titles(url)
    print(games_titles, len(games_titles), "\n")

    games_discounts = crawler.get_games_discounts(url)
    print(games_discounts, len(games_discounts), "\n")

    games_original_prices, games_final_prices = crawler.get_games_prices(url)
    
    print(games_original_prices, len(games_original_prices), "\n")
    print(games_final_prices, len(games_final_prices), "\n")

    games_urls = crawler.get_games_urls(url)
    print(games_urls, len(games_urls))