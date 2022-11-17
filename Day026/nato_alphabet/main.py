import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {key: value for (key, value) in df.values}
# can also use the instructor's method:
# nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_nato = [nato_dict[letter] for letter in word]
print(word_nato)
