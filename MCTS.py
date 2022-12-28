""" An implementation of MCTS and the MCTS Player """


from math import log, sqrt
from platform import node
from random import choice

class Node(object):
    """Node used in MCTS"""

    def __init__(self, state):
        self.state = state
        self.children = {}  # maps moves to Nodes
        self.visits = 0  # number of times node was in select/expand path
        self.wins = 0  # number of wins for player +1
        self.losses = 0  # number of losses for player +1
        self.value = 0  # value (from player +1's perspective)
        self.untried_moves = list(state.availableMoves())  # moves to try

    def updateValue(self, outcome):
        """
        Increments self.visits.
        Updates self.wins or self.losses based on the outcome, and then
        updates self.value.
        This function will be called during the backpropagation phase
        on each node along the path traversed in the selection and
        expansion phases.
        outcome: Who won the game.
                 +1 for a 1st player win
                 -1 for a 2nd player win
                  0 for a draw
        """
        self.visits += 1
        if outcome == 1:
            self.wins += 1
        elif outcome == -1:
            self.losses += 1
        self.value = 1 + (self.wins - self.losses) / self.visits

    def UCBWeight(self, UCB_const, parent_visits, parent_turn):
        """
        Weight from the UCB formula used by parent to select a child.
        This function calculates the weight for JUST THIS NODE. The
        selection phase, implemented by the MCTSPlayer, is responsible
        for looping through the parent Node's children and calling
        UCBWeight on each.

        UCB_const: the C in the UCB formula.
        parent_visits: the N in the UCB formula.
        parent_turn: Which player is making a decision at the parent node.
           If parent_turn is +1, the stored value is already from the
           right perspective. If parent_turn is -1, value needs to be
           converted to -1's perspective.
        returns the UCB weight calculated
        """
        if parent_turn == 1:
            return self.value + (UCB_const * sqrt(log(parent_visits) / self.visits))
        elif parent_turn == -1:
            return 2 - self.value + (UCB_const * sqrt(log(parent_visits) / self.visits))


class MCTSPlayer(object):
    """Selects moves using Monte Carlo tree search."""

    def __init__(self, num_rollouts=1000, UCB_const=1.0):
        self.name = "MCTS"
        self.num_rollouts = int(num_rollouts)
        self.UCB_const = UCB_const
        self.nodes = {}  # dictionary that maps states to their nodes

    def getMove(self, game_state):
        """Returns best move from the game_state after applying MCTS"""

        node_state = str(game_state)
        if node_state in self.nodes.keys():
            curr_node = self.nodes[node_state]
        else:
            curr_node = Node(game_state)
            self.nodes[node_state] = curr_node
        self.MCTS(curr_node)
        bestValue = -float("inf")
        bestMove = None
        for moves, child_node in curr_node.children.items():
            if curr_node.state.turn == 1:
                value = child_node.value
            else:
                value = 2 - child_node.value
            if value > bestValue:
                bestValue = value
                bestMove = moves
        return bestMove

    def status(self, node):
        """
        This method is used solely for debugging purposes. Given a
        node in the MCTS tree, reports on the node's data (wins, losses,
        visits, values), as well as the data of all of its immediate
        children. Helps to verify that MCTS is working properly.
        Returns: None
        """
        print("completed ", self.num_rollouts, " rollouts")
        print("root wins: {wins:6d} losses: {losses:5d}, visits: {visits:5d}, value: {value:3.2f}\
                ".format(wins=node.wins, losses=node.losses, visits=node.visits, \
                         value=node.value))
        for move, child in node.children.items():
            print("Child wins: {wins:5d} losses: {losses:5d}, visits: {visits:5d}, value: {value:3.2f}, move: {move}\
                ".format(wins=child.wins, losses=child.losses, visits=child.visits, \
                         value=child.value, move=move))

    def selection(self, node):

        current_node = node
        path = []
        path.append(current_node)
        while len(current_node.untried_moves) == 0 and not (current_node.state.isTerminal()):
            max_child = (None, float("-inf"))
            for child in current_node.children.values():
                ucb_weight = child.UCBWeight(self.UCB_const, current_node.visits, current_node.state.turn)
                if ucb_weight > max_child[1]:
                    max_child = (child, ucb_weight)
            path.append(max_child[0])
            current_node = max_child[0]

        return path

    def simulation(self, node):
        current_node = node
        while not (current_node.state.isTerminal()):
            current_node = Node(
                current_node.state.makeMove(choice(current_node.untried_moves)))  # state.availableMoves)))
        return current_node.state.winner()

    def expansion(self, node):
        random_move = choice(node.untried_moves)
        node.untried_moves.remove(random_move)
        new_state = node.state.makeMove(random_move)
        node_var = Node(new_state)
        node.children[random_move] = node_var
        self.nodes[str(new_state)] = node_var

        return node_var

    def backpropagation(self, path, outcome):
        for node in path:
            node.updateValue(outcome)

    def MCTS(self, current_node):
        """
        Plays out random games from the current node to a terminal state.
        Each rollout consists of four phases:
        1. Selection: Nodes are selected based on the max UCB weight.
                      Ends when a node is reached where not all children
                      have been expanded.
        2. Expansion: A new node is created for a random unexpanded child.
        3. Simulation: Uniform random moves are played until end of game.
        4. Backpropagation: Values and visits are updated for each node
                     on the path traversed during selection and expansion.
        Returns: None
        """

        for i in range(self.num_rollouts):
            path = self.selection(current_node)
            selected_node = path[-1]
            if selected_node.state.isTerminal():
                outcome = selected_node.state.winner()
            else:
                next_node = self.expansion(selected_node)
                path.append(next_node)
                outcome = self.simulation(next_node)
            self.backpropagation(path, outcome)
        #self.status(current_node)

