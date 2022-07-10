from app import app
from models.game import Game
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()    
    computer_choice = Game.get_computer_move()
    winner = Game.get_winner(player_choice, computer_choice)
    
    return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)
