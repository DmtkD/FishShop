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
        self.frozen_fish_by_price: List[tuple[str, float]] = []
        self.fresh_fish_by_price: List[tuple[str, float]] = []
        self.fish_names_by_price: List[tuple[str, bool, float]] = []

    @singledispatchmethod
    def add_fish(self, args) -> None:
        pass

    @add_fish.register                                                        # ПАСХАЛКА "Тут був автор(-ка) коту/коду"
    def _add_fish(self, fish_box: FishBox) -> None:
        if not self.frozen_fish_boxes:
            self.frozen_fish_boxes[fish_box.name] = [fish_box]
        else:
            for key in self.frozen_fish_boxes:
                count: int = 0
                if key == fish_box.name:
                    self.frozen_fish_boxes[fish_box.name].append(fish_box)
                else:
                    count += 1
                    if count == len(self.fresh_fishes):
                        self.frozen_fish_boxes[fish_box.name] = [fish_box]
                        break

    @add_fish.register
    def _add_fish(self, fish: Fish) -> None:
        if not self.fresh_fishes:
            self.fresh_fishes[fish.name] = [fish]
        else:
            for key in self.fresh_fishes:
                count: int = 0
                if key == fish.name:
                    self.fresh_fishes[fish.name].append(fish)
                else:
                    count += 1
                    if count == len(self.fresh_fishes):
                        self.fresh_fishes[fish.name] = [fish]
                        break

    def get_frozen_fish_names_sorted_by_price(self) -> List[tuple[str, float]]:
        for key in self.frozen_fish_boxes:
            for i in range(len(self.frozen_fish_boxes[key])):
                self.frozen_fish_by_price.append((self.frozen_fish_boxes[key][i].name,
                                                  self.frozen_fish_boxes[key][i].price_in_uah_per_kilo))
        self.frozen_fish_by_price.sort(key=lambda price: price[1])
        return self.frozen_fish_by_price

    def get_fresh_fish_names_sorted_by_price(self) -> List[tuple[str, float]]:
        for key in self.fresh_fishes:
            for i in range(len(self.fresh_fishes[key])):
                self.fresh_fish_by_price.append((self.fresh_fishes[key][i].name,
                                                 self.fresh_fishes[key][i].price_in_uah_per_kilo))
        self.fresh_fish_by_price.sort(key=lambda price: price[1])
        return self.fresh_fish_by_price

    def get_fish_names_sorted_by_price(self) -> List[tuple[str, bool, float]]:
        for key in self.frozen_fish_boxes:
            for i in range(len(self.frozen_fish_boxes[key])):
                self.fish_names_by_price.append((self.frozen_fish_boxes[key][i].name,
                                                 self.frozen_fish_boxes[key][i].is_alive,
                                                 self.frozen_fish_boxes[key][i].price_in_uah_per_kilo))
        for key in self.fresh_fishes:
            for i in range(len(self.fresh_fishes[key])):
                self.fish_names_by_price.append((self.fresh_fishes[key][i].name, True,
                                                 self.fresh_fishes[key][i].price_in_uah_per_kilo))
        self.fish_names_by_price.sort(key=lambda price: price[2])
        return self.fish_names_by_price

    def sell_fish(self, fish_name: str, weight: float, is_fresh: bool) -> None:
        pass

    def cast_out_old_fish(self) -> None:
        for key in self.fresh_fishes:
            for i in range(len(self.fresh_fishes[key])):
                k: int = 0
                if self.fresh_fishes[key][i-k].due_data == date.today():
                    self.fresh_fishes[key].pop(i-k)
                    k += 1
        for key in self.frozen_fish_boxes:
            for i in range(len(self.frozen_fish_boxes[key])):
                k: int = 0
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
