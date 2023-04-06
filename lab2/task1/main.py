import first_task

def main():
    text = input('Enter text: ')
    print('Amount of sentences: ' + str(first_task.amount_of_sentences(text)))
    print('Amount of non-declarative sentences: ' + str(first_task.amount_of_non_declarative_sentences(text)))
    print('Average word length: ' + str(first_task.average_word_lenght(text)))
    print('Average sentence length: ' + str(first_task.average_sentence_lenght(text)))
    print('Top-K repeated N-grams: ' + str(first_task.top_k_repeated_n_grams(text)))


if __name__ == "__main__":
    main()