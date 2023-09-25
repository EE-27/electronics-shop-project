class Keyboard():

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._language = "EN"

    def __str__(self):
        return self.name

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_lang):
        if new_lang not in ("EN", "RU"):
            raise AttributeError("Unsupported language. Supported languages: EN, RU")
        self._language = new_lang