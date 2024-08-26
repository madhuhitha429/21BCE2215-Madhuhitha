from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game import Game

app = Flask(__name__)
socketio = SocketIO(app)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('move')
def handle_move(data):
    character = data['character']
    move = data['move']
    if game.make_move(character, move):
        emit('gameStateUpdate', game.get_game_state(), broadcast=True)
    else:
        emit('invalidMove')

@socketio.on('reset')
def handle_reset():
    game.reset_game()
    emit('gameStateUpdate', game.get_game_state(), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)


