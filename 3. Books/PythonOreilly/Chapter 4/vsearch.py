def search4vowels(word: str) -> set:
    """Возвращает гласные из указанного слова"""
    vowels = set('aeiou')
    return vowels.intersection(sorted(set(list(word))))


def search4letters(phrase: str, letters: str) -> set:
    """Возвращает буквы из данного списка, найденные в указанной фразе"""
    return set(letters).intersection(set(phrase))
