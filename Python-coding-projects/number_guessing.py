import random
def start_game():
    print("Welcome to the number guessing game ")
    print("i am thinking of a number between 1 and 100")
    number = random.randint(1,100)
    attempts = 0
    guessed_correctly = False
    while not guessed_correctly:
        try:
            guess = int(input("enter your guess :"))
            attempts += 1
            if guess < number :
                print("very low ! try again ")
            elif guess > number :
                print("very high ! try again ")
            else:
                print(f"you have guessed the number in {attempts} attempts")
                guessed_correctly = True 
        except ValueError:
            print("please enter a valid number")
if __name__ == "__main__":
    start_game()