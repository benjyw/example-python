import random

from translate import Translator

from util.resource_util import get_lines


class LanguageSelector:
    def __init__(self):
        self._langs = get_lines(__name__, 'langs.txt')

    def _pick_language(self):
        return random.choice(self._langs)

    def translate_to_random_language(self, phrase: str) -> str:
        translator = Translator(self._pick_language())
        return translator.translate(phrase)
