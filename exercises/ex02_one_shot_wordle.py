""" __author__ = 730407527 """

secret_word = "python"
guessed_word = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
yellow_index: int = 0 
yellow_bool: bool = False
emoji_string: str = ""

while len(guessed_word) != len(secret_word): 
    guessed_word = input("That was not 6 letters! Try again: ") 

while index < len(secret_word):
    if guessed_word[index] == secret_word[index]:
        emoji_string = emoji_string + GREEN_BOX
    elif guessed_word[index] != secret_word[index]:
        counter: int = 0
        while counter < len(secret_word):
            if guessed_word[index] == secret_word[counter]:
                yellow_bool = True
            counter = 1 + counter
        if yellow_bool: 
            emoji_string = emoji_string + YELLOW_BOX
            yellow_bool = False
        else: 
            emoji_string = emoji_string + WHITE_BOX
    index = index + 1

print(emoji_string)

if secret_word == guessed_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
