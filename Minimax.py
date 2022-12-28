"""An Implementation of the both MinMax Players """
class MinMaxPlayer:
    """Gets moves by depth-limited min-max search."""
    def __init__(self, boardEval, depthBound):
        self.name = "MinMax"
        self.boardEval = boardEval
        self.depthBound = depthBound

    def bounded_min_max(self, game_state, depth):
        if depth == self.depthBound or game_state.isTerminal():
            return self.boardEval(game_state)
        bestValue = -float("inf") * game_state.turn
        for move in game_state.availableMoves():
            next_state = game_state.makeMove(move)
            value = self.bounded_min_max(next_state, depth+1)
            if game_state.turn == 1:
                if value > bestValue:
                    bestValue = value
                    if depth==0: self.bestMove = move
            else:
                if value < bestValue:
                    bestValue = value
                    if depth==0: self.bestMove = move
        return bestValue
            
    def getMove(self, game_state):
        self.bestMove = None
        value = self.bounded_min_max(game_state, 0)
        #print("bestMove", self.bestMove, "score", value)
        return self.bestMove

class PruningPlayer:
    """Gets moves by depth-limited min-max search with alpha-beta pruning."""
    def __init__(self, boardEval, depthBound):
        self.name = "Pruning"
        self.boardEval = boardEval
        self.depthBound = depthBound

    def alpha_beta(self, game_state, depth, low_bound, up_bound):
        #print("depth", depth, "low", low_bound, "up ", up_bound)
        if depth == self.depthBound or game_state.isTerminal():
            return self.boardEval(game_state)
        bestValue = -float("inf") * game_state.turn
        for move in game_state.availableMoves():
            next_state = game_state.makeMove(move)
            value = self.alpha_beta(next_state, depth+1, low_bound, up_bound)
            if game_state.turn == 1:
                if value > bestValue:
                    bestValue = value
                    if depth==0: self.bestMove = move
                low_bound = max(value, low_bound)
            else:
                if value < bestValue:
                    bestValue = value
                    if depth==0: self.bestMove = move
                up_bound = min(value, up_bound)
            if low_bound >= up_bound:
                #print("**************PRUNED!", low_bound, up_bound)
                break
        return bestValue
        
    def getMove(self, game_state):
        self.bestMove = None
        value = self.alpha_beta(game_state, 0, -float("inf"), float("inf"))
        #print("bestMove", self.bestMove, "score", value)
        return self.bestMove