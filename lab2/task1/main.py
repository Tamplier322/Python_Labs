import first_task

def main():
    text = input('Enter text: ')
    print('Amount of sentences: ' + str(first_task.amount_of_sentences(text)))


if __name__ == "__main__":
    main()