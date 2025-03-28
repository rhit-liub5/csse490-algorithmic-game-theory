import numpy as np
from agt_server.agents.base_agents.rps_agent import RPSAgent
from agt_server.local_games.rps_arena import RPSArena
from agt_server.agents.test_agents.rps.ta_agent.my_agent import TAAgent


class FictitiousPlayAgent(RPSAgent):

    def setup(self):
        self.ROCK, self.PAPER, self.SCISSORS = 0, 1, 2
        self.actions = [self.ROCK, self.PAPER, self.SCISSORS]
        self.opp_action_history = []


    def get_action(self):
        dist = self.predict()
        print(dist)
        best_move = self.optimize(dist)
        return self.actions[best_move]


    def update(self):
        """
        Updates opp action history to be a record of opponent moves
        Rock - 0, Paper - 1, Scissors - 2
        """
        self.opp_action_history = self.get_opp_action_history()


    def predict(self):
        """
        Uses the opponent's previous moves (self.opp_action_history) to generate and return a probability distribution
        over the opponent's next move
        """
        # DONE Return a a probability distribution over the opponent’s next move
        if len(self.opp_action_history) == 0:
            return np.ones(len(self.actions)) / len(self.actions)
        counts = [self.opp_action_history.count(action) for action in self.actions]
        total = sum(counts)
        return np.array(counts) / total

    def optimize(self, dist):
        """
        Given the distribution over the opponent's next move (output of predict) and knowledge of the payoffs (self.calculate_utils),
        Return the best move according to Ficticious Play.
        Please return one of [self.ROCK, self.PAPER, self.SCISSORS]
        """
        # DONE Calculate the expected payoff of each action 
        # and return the action with the highest payoff
        payoff_matrix = np.array([
            [0, -1, 1],   # Rock vs. Rock, Paper, Scissors
            [1, 0, -1],   # Paper vs. Rock, Paper, Scissors
            [-1, 1, 0]    # Scissors vs. Rock, Paper, Scissors
     ])
        expected_payoffs = []
        for action in self.actions:
            payoff = np.dot(payoff_matrix[action], dist)
            expected_payoffs.append(payoff)
        best_action = self.actions[np.argmax(expected_payoffs)]
        return best_action


if __name__ == "__main__":
    agent_name = "Borui Liu" # Please give your agent a name

    agent = FictitiousPlayAgent(agent_name)
    arena = RPSArena(
        num_rounds=1000,
        timeout=1,
        players=[
            agent,
            TAAgent("BOT_AGENT")
        ]
    )
    arena.run()
