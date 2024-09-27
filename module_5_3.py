class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
       return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        floor = 0
        for i in range(1, new_floor):
            if new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                break
            else:
                floor += 1
                print(floor)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, str):
            try:
                return self.number_of_floors == int(other)
            except ValueError:
                return False
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return NotImplemented

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        return NotImplemented

    def __radd__(self, other: int):
        return self.__add__(other)

    def __iadd__(self, other: int):
        return self.__add__(other)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)# __eq__
print(h1 == 10)
print(h1 == "10")

h1 = h1 + 1# __add__
print(h1)
h1 = h1 + h2
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

