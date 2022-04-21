import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
word_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {code.letter: code.code for (letter, code) in word_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter a name:").upper()
    try:
        output_list = [phonetics[letters] for letters in word]
    except KeyError:
        print("Sorry, only alphabets please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()