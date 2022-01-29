""" Classic ordered searching algorithm"""

low: int = 1 
high: int = 100

print("think of a number between 1-100.")
input("press enter to continue...")
playing: bool = True

while playing and low <= high: 
    guess: int = (high + low) // 2
    str_guess: str = str(guess)
    print(str_guess + "?")
    result: str = input("reply yes, higher, lower: ")
    if result == "yes": 
        print("Woo!")
        playing = False
    elif result == "higher": 
        low = guess + 1 
    else:
        high = guess - 1
