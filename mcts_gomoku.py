import mcts
import gomoku

def playMCTSgame():

    ggg = gomoku.GomokuGameState()
    root = mcts.MCTSNode(ggg)
    node = root
    while ggg.winner is None:
        move = mcts.mcts(node, 500000)
        ggg.executeMove(move)
        node = mcts.MCTSNode(ggg)
        print ggg

def playAgainstMCTS():
    ggg = gomoku.GomokuGameState()
    print ggg

    while True:

        move = int(input("Make your move: "))
        ggg.executeMove(move)

        if ggg.winner is not None:
            break

        node = mcts.MCTSNode(ggg)
        computerMove = mcts.mcts(node, 10000)
        ggg.executeMove(computerMove)
        print ggg

        if ggg.winner is not None:
            break

    print ggg
    print "Player", ggg.winner, "wins"

if __name__ == "__main__":

    # playAgainstMCTS()
    playMCTSgame()