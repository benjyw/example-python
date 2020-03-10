
from translate import Translator


class Greeting:
    def __init__(self, greeting: str):
        self._greeting = greeting

    def translated_greeting(self, to_lang: str) -> str:
        translator = Translator(to_lang)
        return translator.translate(self._greeting)

    def greet(self, name: str, to_lang: str=None) -> str:
        greeting = self.translated_greeting(to_lang) if to_lang else self._greeting
        return f'{greeting}, {name}!'
