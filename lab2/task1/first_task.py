import re
from constants import (WORDS, NUMBERS, SENTENCES, NON_DECL_SENTENCES,
                       ABBREVIATIONS1, ABBREVIATIONS2)

def amount_of_sentences(text: str) -> int:
    text = text.lower()
    amount = len(re.findall(SENTENCES, text))

    for abbreviation in ABBREVIATIONS1:
        amount -= text.count(abbreviation)

    for abbreviation in ABBREVIATIONS2:
        amount -= text.count(abbreviation) * 2

    return amount

def amount_of_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_PATTERN, text))


def average_sentence_lenght(text: str) -> float:
    nums = re.findall(NUMBER_PATTERN, text)
    words = [word for word in re.findall(WORD_PATTERN, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    if amount_of_sentences(text) != 0:
        return round(words_len / amount_of_sentences(text), 2)
    else:
        return 0


def average_word_lenght(text: str) -> float:
    words = re.findall(WORD_PATTERN, text)
    words_len_in_characters = sum(len(word) for word in words)

    if len(words) != 0:
        return round(words_len_in_characters / len(words), 2)
    else:
        return 0