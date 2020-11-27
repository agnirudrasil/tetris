class Game:
    def __init__(self, score, current_piece, board_state):
        self.board = [board_state, board_state]
        self.ready = False
        self.score = [score, score]
        self.current_piece = [current_piece, current_piece]

    def update_board(self, player, board_state):
        self.board[player] = board_state

    def update_score(self, player, score):
        self.score[player] = score

    def update_current_piece(self, player, current_piece):
        self.current_piece[player] = current_piece

    def winner(self):
        return self.board[0].is_game_over() or self.board[1].is_game_over()

    def connected(self):
        return self.ready

    def update(self, player, params):
        self.update_board(player, params[0])
        self.update_score(player, params[1])
        self.update_current_piece(player, params[2])
