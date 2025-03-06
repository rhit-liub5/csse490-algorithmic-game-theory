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
        # TODO Return a a probability distribution over the opponent’s next move
        raise NotImplementedError

    def optimize(self, dist):
        """
        Given the distribution over the opponent's next move (output of predict) and knowledge of the payoffs (self.calculate_utils),
        Return the best move according to Ficticious Play.
        Please return one of [self.ROCK, self.PAPER, self.SCISSORS]
        """
        # TODO Calculate the expected payoff of each action 
        # and return the action with the highest payoff
        raise NotImplementedError


if __name__ == "__main__":
    agent_name = ... # Please give your agent a name

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
