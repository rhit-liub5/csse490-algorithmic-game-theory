import numpy as np

from agt_server.agents.base_agents.rps_agent import RPSAgent
from agt_server.local_games.rps_arena import RPSArena
from agt_server.agents.test_agents.rps.ta_agent.my_agent import TAAgent

class ExponentialAgent(RPSAgent):
    def __init__(self, name):
        super(ExponentialAgent, self).__init__(name)
        self.setup()


    def setup(self):
        self.ROCK, self.PAPER, self.SCISSORS  = 0, 1, 2
        self.actions = [self.ROCK, self.PAPER, self.SCISSORS]
        self.my_utils = np.zeros(len(self.actions))
        self.counts = [0, 0, 0]


    @staticmethod
    def softmax(x):
        # Shifting values to avoid nan issues (due to underflow)
        shifted_x = x - np.max(x)
        exp_values = np.exp(shifted_x)
        return exp_values/np.sum(exp_values)


    def get_action(self):
        move_p = self.calc_move_probs()
        my_move = np.random.choice(self.actions, p=move_p)
        return my_move


    def update(self):
        """
        HINT: Update your move history and utility history to help find your best move in calc_move_probs
        """
        my_last_action = self.get_last_action()
        my_last_utility = self.get_last_util()
        self.my_utils[my_last_action] += my_last_utility
        self.counts[my_last_action] += 1


    def calc_move_probs(self):
        """
         Uses your historical average rewards to generate a probability distribution over your next move using
         the Exponential Weights strategy
        """
        # TODO Calculate the average reward for each action over time and return the softmax of it
        raise NotImplementedError


if __name__ == "__main__":
    agent_name = ... # Please give your agent a name
    agent = ExponentialAgent(agent_name)
    arena = RPSArena(
        num_rounds=1000,
        timeout=1,
        players=[
            agent,
            TAAgent("BOT_AGENT")
        ]
    )
    arena.run()
