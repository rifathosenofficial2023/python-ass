import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    

    target_number = random.randint(1, 100)
    
    
    num = 0
    
    while True:
        try:
            
            guessing_num = int(input("\nEnter your guessing number: "))
            num += 1
            
            
            if guessing_num < target_number:
                print("Too low!")
            elif guessing_num > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {num} attempts.")
                break  
        except ValueError:
            
            print("Invalid input! Please enter a valid integer.")


number_guessing_game()
