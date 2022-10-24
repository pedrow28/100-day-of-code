import pandas

# Getting the data

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}

# for (index, row) in alphabet_data.iterrows():
#     print(row.letter)
#     print(row.code)

dictionary_alphabet = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

# print(dictionary_alphabet.items())

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#
# # Solution 1
#
# list_output = []
#
# for i in list_input:
#     if i in dictionary_alphabet.keys():
#         list_output.append(dictionary_alphabet[i])
#
# # Solution 2 - with comprehension
#
# list_output2 = [dictionary_alphabet[item] for item in list_input if item in dictionary_alphabet.keys()]

# Solution 3


def generate_phonetic():
    word = input("Choose a word: ").upper()
    try:
        list_output3 = [dictionary_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters of the alphabet please.")
        generate_phonetic()
    else:
        print(list_output3)

generate_phonetic()