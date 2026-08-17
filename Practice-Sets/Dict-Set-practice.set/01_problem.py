#Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up.

# Hindi to English Dictionary

words = {
    "paani": "water",
    "kitaab": "book",
    "ghar": "house",
    "aam": "mango"
}

word = input("Enter a Hindi word: ")

print(words.get(word, "Word not found"))
print(words[word])