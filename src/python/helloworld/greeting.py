import random

from util.resource_util import get_lines
from helloworld.lang import LanguageSelector


class Greeter:
    def __init__(self):
        self._greeting_selector = GreetingSelector()
        self._language_selector = LanguageSelector()

    def translated_greeting(self) -> str:
        return self._language_selector.translate_to_random_language(self._greeting_selector.pick_greeting())

    def greet(self, name: str) -> str:
        greeting = self.translated_greeting()
        return f'{greeting}, {name}!'


class GreetingSelector:
    def __init__(self):
        self._greetings = get_lines(__name__, 'greetings.txt')

    def pick_greeting(self):
        return random.choice(self._greetings)

