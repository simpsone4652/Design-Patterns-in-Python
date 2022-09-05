from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List




class Alfabet(Iterator):

    _position: int = None

    _reverse: bool = False

    def __init__(self, car: list_car, reverse: bool = False) -> None:
        self._car = car
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
      
        try:
            value = self._car[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class list_car(Iterable):
 

    def __init__(self, car: List[Any] = []) -> None:
        self._car = car

    def __iter__(self) -> Alfabet:
       
        return Alfabet(self._car)

    def reverse_iterator(self) -> Alfabet:
        return Alfabet(self._car, True)

    def add_item(self, item: Any):
        self._car.append(item)


if __name__ == "__main__":
  
    car = list_car()
    car.add_item("1")
    car.add_item("2")
    car.add_item("3")
    car.add_item("4")

    print("Lista dostępnych aut po kolei:")
    print("\n".join(car))
    print("")

    print("Lista dostępnych aut odwrotnie:")
    print("\n".join(car.reverse_iterator()), end="")