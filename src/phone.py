from item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        return "Only Phone objects and their children can be stacked."

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, x):
        if x <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = x
