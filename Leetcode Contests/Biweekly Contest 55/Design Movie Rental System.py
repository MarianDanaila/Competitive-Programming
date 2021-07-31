from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented_movies = defaultdict(SortedList)
        self.shop_movie = {}
        self.rented_movies = SortedList()
        for shop, movie, price in entries:
            self.unrented_movies[movie].add((price, shop))
            self.shop_movie[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        shops = []
        for _, shop in self.unrented_movies[movie][:5]:
            shops.append(shop)
        return shops

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[(shop, movie)]
        self.unrented_movies[movie].remove((price, shop))
        self.rented_movies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[(shop, movie)]
        self.unrented_movies[movie].add((price, shop))
        self.rented_movies.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        movies = []
        for _, shop, movie in self.rented_movies[:5]:
            movies.append([shop, movie])
        return movies
