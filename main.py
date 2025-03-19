import random

class RockPaperScissors:
    def __init__(self):
        self.choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    def get_choice_name(self, choice):
        return self.choices.get(choice, "Invalid")

    def randomizer(self):
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, player1, player2):
        if player1 == player2:
            return "It's a tie!"
        elif (player1 == "R" and player2 == "S") or \
             (player1 == "P" and player2 == "R") or \
             (player1 == "S" and player2 == "P"):
            return "You win!"
        else:
            return "Computer wins!"

# This ensures that the game does not run on import
if __name__ == "__main__":
    game = RockPaperScissors()
    player_choice = input("Enter your choice (R, P, S): ").upper()
    if player_choice in game.choices:
        computer_choice = game.randomizer()
        print("You chose:", game.get_choice_name(player_choice))
        print("Computer chose:", game.get_choice_name(computer_choice))
        print(game.determine_winner(player_choice, computer_choice))
    else:
        print("Invalid choice, please enter R, P, or S.")

    print("Thanks for playing!")