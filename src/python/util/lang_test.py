import pytest

from util.lang import LanguageTranslator


def test_language_translator():
    language_translator = LanguageTranslator()
    assert 'hola' == language_translator.translate('es', 'hello')


def test_unknown_language():
    with pytest.raises(LanguageTranslator.UnknownLanguage):
        LanguageTranslator().translate('xx', 'hello')
