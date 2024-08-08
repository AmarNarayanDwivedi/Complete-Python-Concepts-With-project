'''
Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
'''

Translator = {
    "hum" : "we",
    "mai" : "I",
    "charpahiya" : "car",
    "suno" : "listen"
}

jawab = input("Enter the word you want meaning of " )

print(Translator.get(jawab, None))

print(Translator)