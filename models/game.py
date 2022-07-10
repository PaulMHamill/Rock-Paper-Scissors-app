import random

class Game():

    def get_computer_move():
        options = ["rock", "paper", "scissors"]
        return options[random.randint(0,2)]

    def get_winner(player_choice, computer_choice):
        winner = "computer"

        if player_choice == computer_choice:
            winner = "tie"
        if player_choice == "rock" and computer_choice == "scissors":
            winner = "player"
        if player_choice == "scissors" and computer_choice == "paper":
            winner = "player"
        if player_choice == "paper" and computer_choice == "rock":
            winner = "player"

        return winner

            

