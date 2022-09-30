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

word = input().upper()

list_input = list(word)

# Solution 1

list_output = []

for i in list_input:
    if i in dictionary_alphabet.keys():
        list_output.append(dictionary_alphabet[i])

# Solution 2 - with comprehension

list_output2 = [dictionary_alphabet[item] for item in list_input if item in dictionary_alphabet.keys()]

# Solution 3

list_output3 = [dictionary_alphabet[letter] for letter in word]

print(list_output)
print(list_output2)
print(list_output3)

