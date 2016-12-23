
class GomokuGameState(object):

    def __init__(self):
        self.currentPlayer = 1
        self.width = 5
        self.board = [0] * self.width * self.width
        self.winner = None

    def copy(self):
        gamestate = GomokuGameState()
        gamestate.board = list(self.board)
        gamestate.currentPlayer = self.currentPlayer
        gamestate.winner = self.winner

        return gamestate

    def executeMove(self, move):
        assert self.winner is None

        self.board[move] = self.currentPlayer
        self.currentPlayer = 3 - self.currentPlayer
        self.checkForWin()

    def getLegalMoves(self):
        return filter(lambda x: self.board[x] == 0, xrange(len(self.board)))

    def checkForWin(self):

        for i in range(self.width * self.width):
            if i % self.width <= (self.width - 5):  # horizon
                if self.board[i] == self.board[i+1] == self.board[i+2] == self.board[i+3] == self.board[i+4]:
                    if self.board[i] != 0:
                        self.winner = self.board[i]
                        break
            if i / self.width <= (self.width - 5):  # vertical
                if self.board[i] == self.board[i + self.width] == self.board[i + 2*self.width] == self.board[i + 3*self.width] == self.board[i + 4*self.width]:
                    if self.board[i] != 0:
                        self.winner = self.board[i]
                        break
            if i % self.width <= (self.width - 5) and i / self.width <= (self.width - 5):
                if self.board[i] == self.board[i + self.width + 1] == self.board[i + 2*self.width + 2] == self.board[i + 3*self.width + 3] == self.board[i + 4*self.width + 4]:
                    if self.board[i] != 0:
                        self.winner = self.board[i]
                        break

        if self.winner is None and self.getLegalMoves() == []:
            self.winner = 0

    def __repr__(self):
        icons = ['-', 'x', 'o']
        iconBoard = [icons[i] for i in self.board]
        for i in (25, 20, 15, 10, 5):
            iconBoard.insert(i, "\n")
        return ''.join(iconBoard)