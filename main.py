from datetime import date
from typing import List
from functools import singledispatchmethod


class FishInfo:
    def __init__(self, name: str, origin: str, price_in_uah_per_kilo: float, catch_date: List[int],
                 due_date: List[int]) -> None:
        self.name = name
        self.origin = origin
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = date(*catch_date)
        self.due_date = date(*due_date)


class Fish(FishInfo):

    def __init__(self, age_in_months: float, weight: float, name: str, origin: str, price_in_uah_per_kilo: float,
                 catch_date: List[int], due_date: List[int]) -> None:
        super().__init__(name, origin, price_in_uah_per_kilo, catch_date, due_date)
        self.age_in_months = age_in_months
        self.weight = weight

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return "Fish info, name: {0}, origin: {1}, price={2}".format(self.name, self.origin, self.price_in_uah_per_kilo)


class FishBox(FishInfo):

    def __init__(self, weight: float, height: float, length: float, depth: float, is_alive: bool, name: str,
                 origin: str, price_in_uah_per_kilo: float, catch_date: List[int], due_date: List[int]) -> None:
        super().__init__(name, origin, price_in_uah_per_kilo, catch_date, due_date)
        self.weight = weight
        self.height = height
        self.length = length
        self.depth = depth
        self.is_alive = is_alive


class FishShop:

    def __init__(self) -> None:
        self.frozen_fish_boxes: dict[str: list[FishBox]] = {}
        self.fresh_fishes: dict[str: list[Fish]] = {}
        self.fish_names_by_price: List[tuple[str, bool, float]] = []

    @singledispatchmethod
    def add_fish(self, args) -> None:
        pass

    @add_fish.register                                                        # ПАСХАЛКА "Тут був автор(-ка) коту/коду"
    def _add_fish(self, fish_box: FishBox) -> None:
        self.fresh_fishes.setdefault(fish_box.name, []).append(fish_box)

    @add_fish.register
    def _add_fish(self, fish: Fish) -> None:
        self.fresh_fishes.setdefault(fish.name, []).append(fish)

    def get_frozen_fish_names_sorted_by_price(self) -> List[tuple[str, float]]:
        frozen_fish_by_price = []
        for key in self.frozen_fish_boxes:
            for i in range(len(self.frozen_fish_boxes[key])):
                frozen_fish_by_price.append((self.frozen_fish_boxes[key][i].name,
                                             self.frozen_fish_boxes[key][i].price_in_uah_per_kilo))
        frozen_fish_by_price.sort(key=lambda price: price[1])
        return frozen_fish_by_price

    def get_fresh_fish_names_sorted_by_price(self) -> List[tuple[str, float]]:
        fresh_fish_by_price = []
        for key in self.fresh_fishes:
            for i in range(len(self.fresh_fishes[key])):
                fresh_fish_by_price.append((self.fresh_fishes[key][i].name,
                                            self.fresh_fishes[key][i].price_in_uah_per_kilo))
        fresh_fish_by_price.sort(key=lambda price: price[1])
        return fresh_fish_by_price

    def get_fish_names_sorted_by_price(self) -> List[tuple[str, bool, float]]:
        fish_names_by_price = []
        for key in self.frozen_fish_boxes:
            for i in range(len(self.frozen_fish_boxes[key])):
                fish_names_by_price.append((self.frozen_fish_boxes[key][i].name,
                                            self.frozen_fish_boxes[key][i].is_alive,
                                            self.frozen_fish_boxes[key][i].price_in_uah_per_kilo))
        for key in self.fresh_fishes:
            for i in range(len(self.fresh_fishes[key])):
                fish_names_by_price.append((self.fresh_fishes[key][i].name, True,
                                            self.fresh_fishes[key][i].price_in_uah_per_kilo))
        fish_names_by_price.sort(key=lambda price: price[2])
        return fish_names_by_price

    def sell_fish(self, fish_name: str, weight: float, is_fresh: bool) -> None:
        pass

    def cast_out_old_fish(self) -> None:
        for key in self.fresh_fishes:
            k: int = 0
            for i in range(len(self.fresh_fishes[key])):
                if self.fresh_fishes[key][i-k].due_data == date.today():
                    self.fresh_fishes[key].pop(i-k)
                    k += 1
        for key in self.frozen_fish_boxes:
            k: int = 0
            for i in range(len(self.frozen_fish_boxes[key])):
                if self.frozen_fish_boxes[key][i-k] == date.today():
                    self.frozen_fish_boxes[key].pop(i-k)
                    k += 1


class Seller:

    def check_fish_in_store(self, fish_name) -> bool:
        pass

    def sell_fish(self, price: float) -> None:
        pass


class Buyer:

    def buy_fish(self, fish_name: str, weigh_of_fish: float) -> float:
        pass

    def check_money_for_buying(self, price: float) -> bool:
        pass


fishes = Fish(10, 20, "Oleg", "Ukraine", 200, [2020, 12, 12], [2030, 12, 31])
fishes2 = Fish(10, 20, "Oleg", "Ukraine", 150, [2021, 12, 12], [2030, 12, 31])
fishes3 = Fish(10, 20, "Ol", "Ukraine", 170, [2021, 12, 12], [2030, 12, 31])
shop = FishShop()
shop.add_fish(fishes)
shop.add_fish(fishes2)
shop.add_fish(fishes3)
print(shop.fresh_fishes)