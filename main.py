from datetime import date
import datetime
from typing import List


class Fish:

    def __init__(self, name: str = "", price_in_uah_per_kilo: float = 0, catch_date: List[int] = (2022, 1, 12),
                 origin: str = "", body_only: bool = False, weight: float = 0) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = date(*catch_date)
        self.origin = origin
        self.body_only = body_only
        self.weight = weight


class FishShop:

    def __init__(self):
        self.__list_of_fish = []
        self.list_for_selling = {}
        self.__total_price = 0

    def create_list(self, *args: Fish) -> None:
        for arg in args:
            self.__list_of_fish.append(arg)

    def add_fish_for_selling(self, fish_name: str, total_weight: float) -> None:
        for i in range(len(self.__list_of_fish)):
            if self.__list_of_fish[i].name == fish_name:
                self.list_for_selling[fish_name] = total_weight                # ПАСХАЛКА "Тут був автор(-ка) коту/коду"

    def get_fish_names_sorted_by_price(self) -> List[Fish]:
        self.__list_of_fish.sort(key=lambda fish: fish.price_in_uah_per_kilo)
        return self.__list_of_fish

    def sell_fish(self, fish_name: str, weight: float) -> float:
        for i in range(len(self.__list_of_fish)):
            if self.__list_of_fish[i].name == fish_name:
                self.__total_price += self.__list_of_fish[i].price_in_uah_per_kilo * weight
                self.__list_of_fish[i].weight -= weight
        return self.__total_price

    def cast_out_old_fish(self) -> List[Fish]:
        k: int = 0
        for i in range(len(self.__list_of_fish)):
            if date.today() - self.__list_of_fish[i - k].catch_date > datetime.timedelta(10):
                self.__list_of_fish.pop(i - k)
                k += 1
        return self.__list_of_fish


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
