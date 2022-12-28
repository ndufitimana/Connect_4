"""
The following interface for board games was obtained from Professor Lisa Meeden 
of Swarthmore College Computer Science Department. 
https://www.cs.swarthmore.edu/~meeden/ 
"""
from ConnectGame import ConnectGame
from GamePlayers import HumanPlayer, RandomPlayer
from argparse import ArgumentParser
from MCTS import MCTSPlayer
from Minimax import MinMaxPlayer, PruningPlayer
from StaticEvals import connectBasicEval
import pylab

games = {"connect": ConnectGame}

players = {"random": RandomPlayer,
           "human": HumanPlayer,
           "mcts": MCTSPlayer,
           "minmax": MinMaxPlayer,
           "pruning": PruningPlayer
           }
eval_options = ["basic"]

eval_functions = {"connect":{"basic":connectBasicEval
                             }}

def main():
    args = parse_args()
    fp = open("result.txt", "a")
    fp.write(str(args ) + "\n")
    if args.p1 in  ["minmax", "pruning"]  or args.p2 in  ["minmax", "pruning"]:
        if args.p1 == "minmax" or args.p1 == "pruning":
            e1 = eval_functions[args.game][args.e1]
            p1 = players[args.p1](e1, args.d1)
        else:
            p1 = players[args.p1](*args.a1)
        if args.p2 == "minmax" or args.p2 == "pruning":
            e2 = eval_functions[args.game][args.e2]
            p2 = players[args.p2](e2, args.d2)
            
        else:
            p2 = players[args.p2](*args.a2)
    else:
        p1 = players[args.p1](*args.a1)
        p2 = players[args.p2](*args.a2)
    
    game = games[args.game](*args.game_args)

    if args.games == 1:
        play_game(game, p1, p2, True)
    else:
        
        p1_wins = 0
        p2_wins = 0
        draws = 0
        for i in range(args.games):
            if i % 2:
                result = play_game(game, p1, p2, False)
                if result.winner() == 1:
                    p1_wins += 1
                   
                elif result.winner() == -1:
                    p2_wins += 1
                    
                else:
                    draws += 1
            else:
                result = play_game(game, p2, p1, False)
                if result.winner() == -1:
                    p1_wins += 1
                elif result.winner() == 1:
                    p2_wins += 1
                else:
                    draws += 1
        
        
        print("results after", args.games, "games:")
        print(p1_wins, "wins for player 1 (" + p1.name + ")")
        print(p2_wins, "wins for player 2 (" + p2.name + ")")
        fp.write("%s %d \n"% (p1.name, p1_wins))
        fp.write("%s %d \n"% (p2.name, p2_wins))
        if draws > 0:
            print(draws, "draws")
        fp.close()
def plotStats(games, player1wins, player2wins, title=""):
    """
    Plots a summary statics for both players over multiple games.
    Adds the given title to the plot. 
    """
    totalGames = range(games)
    pylab.plot(totalGames, player1wins, label="Player1")
    pylab.plot(totalGames, player2wins, label="Player2")
    pylab.legend(loc="upper left")
    pylab.xlabel("Total Games")
    pylab.ylabel("Total Wins")
    if len(title) != 0:
        pylab.title(title)
    pylab.savefig("multipleGamesStat.png")
    pylab.show()


def parse_args():
    p = ArgumentParser()
    p.add_argument("game", type=str, choices=list(games.keys()),
                   help="Game to be played.")
    p.add_argument("p1", type=str, choices=list(players.keys()),
                   help="Player 1 type.")
    p.add_argument("p2", type=str, choices=list(players.keys()),
                   help="Player 2 type.")
    p.add_argument("-a1", nargs="*", type=float, default=[],
                   help="Arguments for player 1.")
    p.add_argument("-a2", nargs="*", type=float, default=[],
                   help="Arguments for player 2.")
    p.add_argument("-games", type=int, default=1,
                   help="Number of games to play.")
    p.add_argument("-game_args", type=int, nargs="*", default=[],
                   help="Optional arguments to pass to the game constructor, " +"such as board dimensions. Must be listed in order.")
    p.add_argument("-e1", type=str, choices=eval_options, default="basic",
                   help="Board eval function for player 1.")
    p.add_argument("-e2", type=str, choices=eval_options, default="basic",
                   help="Board eval function for player 2.")
    p.add_argument("-d1", type=int, default=4,
                   help="Search depth for player 1.")
    p.add_argument("-d2", type=int, default=4,
                   help="Search depth for player 2.")
    p.add_argument("--show", action="store_true", help=
                   "Set this flag to print the board every round.")
    
    return p.parse_args()


def play_game(game, player1, player2, show=False):

    """Plays a game then returns the final state."""

    while not game.isTerminal():
        if show:
            print(game)

        if game.turn == 1:
            m = player1.getMove(game)
        else:
            m = player2.getMove(game)
        if m not in game.availableMoves():
            raise Exception("invalid move: " + str(m))
        game = game.makeMove(m)
        if show:
            print("Move:", m, "\n")
    if show:
        print(game, "\n")
        if game.winner() != 0:
            print("player", game._print_char(game.winner()), "(", end='')
            print((player1.name if game.winner() == 1 else player2.name) + ") wins")
        else:
            print("it's a draw")
    return game


if __name__ == "__main__":
    main()
