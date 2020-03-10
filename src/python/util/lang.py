import random

from translate import Translator
from util.resources import get_lines


class LanguageTranslator:
    class UnknownLanguage(Exception):
        pass

    def __init__(self):
        self._langs = get_lines(__name__, "langs.txt")

    def translate(self, lang: str, phrase: str) -> str:
        if lang not in self._langs:
            raise self.UnknownLanguage(lang)
        translator = Translator(lang)
        return translator.translate(phrase)

    def translate_to_random_language(self, phrase: str) -> str:
        return self.translate(self._pick_random_language(), phrase)

    def _pick_random_language(self):
        return random.choice(self._langs)
