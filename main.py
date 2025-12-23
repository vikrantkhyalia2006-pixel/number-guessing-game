from random import randint

def number_guessing_game():
    num_guess = randint(1, 100)
    guess_count = 0
    while True:
        while True:
            try:
                user_input = int(input("Enter a number (1 to 100): "))

            except ValueError:
                print("Please enter a valid number.")
                continue # restart loop for invalid input

            if (user_input<1 or user_input>100):
                print("Number must be between 1 and 100.")
                continue

            guess_count += 1
            
            if(user_input < num_guess):
                print("too low!")

            elif(user_input > num_guess):
                print("too high!")  

            else:
                print(f"Congratulations you guessed the correct number {num_guess} in {guess_count} tries!")
                break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thanks for playing!")
            break
    

    
number_guessing_game()