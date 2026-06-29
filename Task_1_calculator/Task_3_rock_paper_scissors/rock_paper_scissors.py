import random

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        return "rock"
    elif choice == '2':
        return "paper"
    elif choice == '3':
        return "scissors"
    else:
        print("Invalid choice, try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScoreboard:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing!")
            break
        round_number += 1

def main():
    print("="*50)
    print("🎮 Welcome to Rock-Paper-Scissors 🎮")
    print("="*50)
    print("Instructions:")
    print("- Rock beats Scissors")
    print("- Scissors beat Paper")
    print("- Paper beats Rock")
    print("Try to beat the computer!\n")
    play_game()

if __name__ == "__main__":
    main()
