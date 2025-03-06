# Lab 1: Learning Agents for Repeated Games
If you have not already done so, set up your Python environment using the instructions in the root-level README.

## Agent Methods 
For the `RPSAgent`, here are a few methods that you may find helpful! 
- `self.calculate_utils(a1, a2)` is a method that takes in player 1's action (`a1`) and player 2's action (`a2`) and returns a list [`u1`, `u2`] where `u1` is player1's utility and `u2` is player 2's utility. 
    - For example `self.calculate_utils(self.ROCK, self.PAPER)` would return `[-1, 1]`
- `self.get_action_history()` is a method that returns a list of your actions from previous rounds played.
- `self.get_util_history()` is a method that returns a list of your utility from previous rounds played. 
- `self.get_opp_action_history()` is a method that returns a list of your opponent's actions from previous rounds played.
- `self.get_opp_util_history()` is a method that returns a list of your opponent's utility from previous rounds played.
- `self.get_last_action()` is a method that returns a your last action from the previous round.
- `self.get_last_util()` is a method that returns a your last utility from the previous round.
- `self.get_opp_action_history()` is a method that returns a your opponent's last action from the previous round.
- `self.get_opp_util_history()` is a method that returns a your opponent's last utility from the previous round.
