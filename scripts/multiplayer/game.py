class Game:
    def __init__(self, score, current_piece, board_state):
        self.board = board_state
        self.score = score
        self.current_piece = current_piece

    def update_board(self, board_state):
        self.board = board_state

    def update_score(self, score):
        self.score = score

    def update_current_piece(self, current_piece):
        self.current_piece = current_piece

    def winner(self):
        return self.board.is_game_over()
