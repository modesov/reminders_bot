from bot.lexicon.en import en
from bot.lexicon.ru import ru


def get_text(*, alias: str, language: str = 'ru'):
    languages = {
        'ru': ru,
        'en': en
    }
    return languages.get(language).get(alias, '-') \
        if languages.get(language, False) else languages.get('ru').get(alias, '-')
