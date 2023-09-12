import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name  # private __
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        cls.all = []

        with open(csv_file) as file:
            dictread = csv.DictReader(file)
            for line in dictread:
                name = line["name"]
                price = int(line["price"])
                quantity = int(line["quantity"])
                item = cls(name, price, quantity)



        # with open(csv_file, "r") as file:
        #     next(file)  # Skip the header line... Thank you, ChatGPT
        #
        #     for line in file:
        #         name, price, quantity = line.split(",")
        #         price = cls.string_to_number(price)
        #         item = cls(name, price, quantity)
        #         items.append(item)
        # return items

    @staticmethod
    def string_to_number(price):
        if isinstance(price, str):
            return int(float(price))
