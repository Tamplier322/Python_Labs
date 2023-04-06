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
    return len(re.findall(NON_DECL_SENTENCES, text))


def average_sentence_lenght(text: str) -> float:
    nums = re.findall(NUMBERS, text)
    words = [word for word in re.findall(WORDS, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    if amount_of_sentences(text) != 0:
        return round(words_len / amount_of_sentences(text), 2)
    else:
        return 0


def average_word_lenght(text: str) -> float:
    words = re.findall(WORDS, text)
    words_len_in_characters = sum(len(word) for word in words)

    if len(words) != 0:
        return round(words_len_in_characters / len(words), 2)
    else:
        return 0

def top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(WORDS, text.lower())
    dictOfNgrams = {}
    for i in range(len(words) - n + 1):
        n_gram = ' '.join([str(word) for word in words[i:i + n]])
        if n_gram not in dictOfNgrams:
            dictOfNgrams[n_gram] = 1
        else:
            dictOfNgrams[n_gram] += 1
    sorted_ngrams = sorted(dictOfNgrams.items(), key=lambda x: x[1], reverse=True)
    return sorted_ngrams[0:k]