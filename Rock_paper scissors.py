import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    draws = 0

    print("=" * 40)
    print("      ROCK PAPER SCISSORS GAME")
    print("=" * 40)

    while True:

        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_choice = input("Enter your choice (1-4): ").strip()
        if user_choice == "4":
            break
        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        player_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)

        print("\nYou chose:", player_choice.capitalize())
        print("Computer chose:", computer_choice.capitalize())

        if player_choice == computer_choice:
            print("Result: It's a Draw!")
            draws += 1

        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            print("Result: You Win!")
            player_score += 1

        else:
            print("Result: Computer Wins!")
            computer_score += 1

        print("\n----- SCOREBOARD -----")
        print("Your Score:", player_score)
        print("Computer Score:", computer_score)
        print("Draws:", draws)

    print("\n" + "=" * 40)
    print("           FINAL RESULTS")
    print("=" * 40)
    print("Your Score:", player_score)
    print("Computer Score:", computer_score)
    print("Total Draws:", draws)

    if player_score > computer_score:
        print("Overall Result: You are the winner!")
    elif computer_score > player_score:
        print("Overall Result: Computer is the winner!")
    else:
        print("Overall Result: The game is tied!")

    print("\nThank you for playing!")

play_game()
