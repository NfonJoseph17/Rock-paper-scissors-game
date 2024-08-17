import random

# Initialize scores
user_win = 0
comp_win = 0
options = ['rock', 'paper', 'scissors']

# Game loop
while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_choice == "q":
        break
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(options)
    print(f"Computer picked: {computer_choice.capitalize()}")

    # Determine the winner
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
        user_win += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lost!")
        comp_win += 1

# Display final scores
print(f"\nFinal Scores: You won {user_win} times, Computer won {comp_win} times.")
print("Goodbye!")