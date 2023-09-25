from item import Item


class MixinLog:
    def __init__(self):
        pass

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = "EN"

    def __str__(self):
        return self.name


    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_lang):
        if new_lang not in ("EN", "RU"):
            raise AttributeError("Unsupported language. Supported languages: EN, RU")
        self._language = new_lang
