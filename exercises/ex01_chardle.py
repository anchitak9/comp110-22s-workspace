"""EXO1 - Chardle - A cute step toward Wordle."""
__author__ = "730407527"

guessed_word: str = input("Enter a 5-character word: ")
if len(guessed_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

guessed_character: str = input("Enter a single character: ")

if len(guessed_character) != 1: 
    print("Error: Character must be a single character.")
    quit()

print("Searching for " + guessed_character + " in " + guessed_word)
number_matches: int = 0

if guessed_word[0] == guessed_character:
    print(guessed_character + " found at index 0")
    number_matches = number_matches + 1

if guessed_word[1] == guessed_character: 
    print(guessed_character + " found at index 1")
    number_matches = number_matches + 1

if guessed_word[2] == guessed_character: 
    print(guessed_character + " found at index 2")
    number_matches = number_matches + 1

if guessed_word[3] == guessed_character: 
    print(guessed_character + " found at index 3")
    number_matches = number_matches + 1

if guessed_word[4] == guessed_character: 
    print(guessed_character + " found at index 4")
    number_matches = number_matches + 1

if number_matches >= 2:
    print(str(number_matches) + " instances of " + guessed_character + " found in " + guessed_word)
else: 
    if number_matches == 1:
        print(str(number_matches) + " instance of " + guessed_character + " found in " + guessed_word)
    else: 
        if number_matches == 0:
            print("No instances of " + guessed_character + " found in " + guessed_word)
