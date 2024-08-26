class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.board = [
            ['A-P1', 'A-P2', 'A-H1', 'A-H2', 'A-H3'],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['B-P1', 'B-P2', 'B-H1', 'B-H2', 'B-H3']
        ]
        self.current_player = 'A'
        self.winner = None
        self.move_history = {'A': [], 'B': []}

    def find_character_position(self, character):
        for i, row in enumerate(self.board):
            if character in row:
                return i, row.index(character)
        return None

    def calculate_new_position(self, char_pos, character, move):
        x, y = char_pos
        move_map = {
            'F': (-1, 0), 'B': (1, 0), 'L': (0, -1), 'R': (0, 1),
            'FL': (-1, -1), 'FR': (-1, 1), 'BL': (1, -1), 'BR': (1, 1),
            'RF': (-1, 2), 'RB': (1, 2), 'LF': (-1, -2), 'LB': (1, -2)
        }
        
        if character.endswith('H3'):
            if move in ['FL', 'FR', 'BL', 'BR', 'RF', 'RB', 'LF', 'LB']:
                if move in ['FL', 'FR']:
                    x -= 2
                    y += 1 if move == 'FR' else -1
                elif move in ['BL', 'BR']:
                    x += 2
                    y += 1 if move == 'BR' else -1
                elif move in ['RF', 'RB']:
                    y += 2
                    x += 1 if move == 'RB' else -1
                elif move in ['LF', 'LB']:
                    y -= 2
                    x += 1 if move == 'LB' else -1
                return x, y

        dx, dy = move_map.get(move, (0, 0))
        return x + dx, y + dy

    def is_valid_move(self, character, move):
        char_pos = self.find_character_position(character)
        if not char_pos:
            return False
        new_pos = self.calculate_new_position(char_pos, character, move)
        x, y = new_pos
        if not (0 <= x < 5 and 0 <= y < 5):
            return False
        return True

    def capture_piece(self, x, y):
        self.board[x][y] = ''

    def check_win(self):
        a_pieces = sum(1 for row in self.board for cell in row if cell.startswith('A'))
        b_pieces = sum(1 for row in self.board for cell in row if cell.startswith('B'))
        return a_pieces == 0 or b_pieces == 0

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def make_move(self, character, move):
        if not self.is_valid_move(character, move):
            return False

        char_pos = self.find_character_position(character)
        new_pos = self.calculate_new_position(char_pos, character, move)
        x, y = new_pos

        self.move_history[self.current_player].append(f"{character} to {move} ({new_pos})")

        target_cell = self.board[x][y]
        if target_cell and target_cell[0] != self.current_player:
            self.capture_piece(x, y)
            self.move_history[self.current_player].append(f"Captured {target_cell} at ({x}, {y})")

        self.board[x][y] = character
        self.board[char_pos[0]][char_pos[1]] = ''

        if self.check_win():
            self.winner = self.current_player

        self.switch_player()
        return True

    def get_game_state(self):
        return {
            'board': self.board,
            'current_player': self.current_player,
            'winner': self.winner,
            'move_history': self.move_history
        }
