import itertools
import unittest
from agent import Agent, AdditiveAgent
from allocation import Allocation
from algorithms import round_robin, envy_cycle_elimination

class TestAgent(unittest.TestCase):

    def test_envies(self):
        valuation = {
            frozenset([1]): 1, 
            frozenset([2]): 2, 
            frozenset([3]): 3, 
            frozenset([4]): 4, 
            frozenset([5]): 5
        }

        agent_one = AdditiveAgent("Agent 1", valuation)
        agent_two = AdditiveAgent("Agent 2", valuation)

        agent_one.add_to_bundle(1)
        agent_one.add_to_bundle(2)
        agent_two.add_to_bundle(3)

        self.assertFalse(agent_one.envies(agent_two))
        self.assertFalse(agent_two.envies(agent_one))

        agent_one.add_to_bundle(4)
        agent_two.add_to_bundle(5)
        self.assertTrue(agent_one.envies(agent_two))
        self.assertFalse(agent_two.envies(agent_one))

    
    def test_envies_up_to_one(self):
        valuation = {
            frozenset([1]): 1, 
            frozenset([2]): 2, 
            frozenset([3]): 3, 
            frozenset([4]): 4, 
            frozenset([5]): 5
        }

        agent_one = AdditiveAgent("Agent 1", valuation)
        agent_two = AdditiveAgent("Agent 2", valuation)

        agent_one.add_to_bundle(1)
        agent_one.add_to_bundle(4)
        
        agent_two.add_to_bundle(2)
        agent_two.add_to_bundle(3)
        agent_two.add_to_bundle(5)      

        self.assertTrue(agent_one.envies(agent_two))
        self.assertFalse(agent_one.envies_up_to_one(agent_two))
        self.assertFalse(agent_two.envies(agent_one))
        self.assertFalse(agent_two.envies_up_to_one(agent_one))


class TestRoundRobin(unittest.TestCase):

    def test_round_robin_additive_identical(self):
        valuation = {
            frozenset([1]): 1, 
            frozenset([2]): 2, 
            frozenset([3]): 3, 
            frozenset([4]): 4, 
            frozenset([5]): 5
        }

        agent_one = AdditiveAgent("Agent 1", valuation)
        agent_two = AdditiveAgent("Agent 2", valuation)
        agent_three = AdditiveAgent("Agent 3", valuation)

        rr_alloc = Allocation(num_items=5, agents=[agent_one, agent_two, agent_three], proc=round_robin)
        rr_alloc.allocate()
        
        # Check for EF1 and PROP1
        self.assertTrue(rr_alloc.is_ef1(), "Round-robin allocation is not EF1")
        self.assertTrue(rr_alloc.is_prop1(), "Round-robin allocation is not PROP1")


    def test_round_robin_additive(self):
        first_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 15, 
            frozenset([3]): 9, 
            frozenset([4]): 8, 
            frozenset([5]): 3
        }

        second_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 8, 
            frozenset([3]): 15, 
            frozenset([4]): 9, 
            frozenset([5]): 4
        }

        third_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 9, 
            frozenset([3]): 8, 
            frozenset([4]): 15, 
            frozenset([5]): 5
        }

        agent_one = AdditiveAgent("Agent 1", first_valuation)
        agent_two = AdditiveAgent("Agent 2", second_valuation)
        agent_three = AdditiveAgent("Agent 3", third_valuation)

        rr_alloc = Allocation(num_items=5, agents=[agent_one, agent_two, agent_three], proc=round_robin)
        rr_alloc.allocate()
        
        # Check for EF1 and PROP1
        self.assertTrue(rr_alloc.is_ef1(), "Round-robin allocation is not EF1")
        self.assertTrue(rr_alloc.is_prop1(), "Round-robin allocation is not PROP1")
    

    def test_round_robin_nonadditive(self):
        # See description of "Two Adventurers" scenario with nonadditive valuations 
        # in the lab instructions, inspired by Avrim Blum's lecture notes: 
        # https://home.ttic.edu/~avrim/AGT24/Lecture%2014%20-%20Fair%20Division2.pdf
        # Round-robin should give an allocation which is PROP1 but not EF1. 
        
        valuation = {}
        num_items = 8
        items = [i for i in range(1, num_items + 1)]
        for size in range(1, num_items + 1):
            for combo in itertools.combinations(items, size):
                if size <= 2 or 2 in combo or 4 in combo:
                    valuation[frozenset(combo)] = size
                else: 
                    valuation[frozenset(combo)] = 2

        adventurer_one = Agent("Adventurer 1", valuation)
        adventurer_two = Agent("Adventurer 2", valuation)

        rr_alloc = Allocation(num_items=num_items, agents=[adventurer_one, adventurer_two], proc=round_robin)
        rr_alloc.allocate()

        # print(rr_alloc) TODO: feel free to uncomment to see the allocation

        # Check for EF1 and PROP1
        self.assertFalse(rr_alloc.is_ef1(), "Round-robin allocation should *not* be EF1 for adventurers' nonadditive valuations")
        self.assertTrue(rr_alloc.is_prop1(), "Round-robin allocation should be PROP1 for adventurers' nonadditive valuations")


class TestEnvyCycle(unittest.TestCase):
    
    def test_envy_cycle_additive(self):
        first_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 15, 
            frozenset([3]): 9, 
            frozenset([4]): 8, 
            frozenset([5]): 3
        }

        second_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 8, 
            frozenset([3]): 15, 
            frozenset([4]): 9, 
            frozenset([5]): 4
        }

        third_valuation = {
            frozenset([1]): 10, 
            frozenset([2]): 9, 
            frozenset([3]): 8, 
            frozenset([4]): 15, 
            frozenset([5]): 5
        }

        agent_one = AdditiveAgent("Agent 1", first_valuation)
        agent_two = AdditiveAgent("Agent 2", second_valuation)
        agent_three = AdditiveAgent("Agent 3", third_valuation)

        ec_alloc = Allocation(num_items=5, agents=[agent_one, agent_two, agent_three], proc=envy_cycle_elimination)
        ec_alloc.allocate() # TODO: Feel free to add "visualize=True" parameter while debugging
        
        # Check for EF1 and PROP1
        self.assertTrue(ec_alloc.is_ef1(), "Envy cycle allocation is not EF1")
        self.assertTrue(ec_alloc.is_prop1(), "Envy cycle allocation is not PROP1")


    def test_envy_cycle_nonadditive(self):
        # See description of "Two Adventurers" scenario with nonadditive valuations 
        # in the lab instructions, inspired by Avrim Blum's lecture notes: 
        # https://home.ttic.edu/~avrim/AGT24/Lecture%2014%20-%20Fair%20Division2.pdf
        # Envy-cycle elimination should give an allocation which is EF1 (and may or may not be PROP1). 
        
        valuation = {}
        num_items = 8
        items = [i for i in range(1, num_items + 1)]
        for size in range(1, num_items + 1):
            for combo in itertools.combinations(items, size):
                # Bags of holding are items 2 and 4
                # All other items are Swords
                if size <= 2 or 2 in combo or 4 in combo:
                    valuation[frozenset(combo)] = size
                else: 
                    valuation[frozenset(combo)] = 2

        adventurer_one = Agent("Adventurer 1", valuation)
        adventurer_two = Agent("Adventurer 2", valuation)

        ec_alloc = Allocation(num_items=num_items, agents=[adventurer_one, adventurer_two], proc=envy_cycle_elimination)
        ec_alloc.allocate() # TODO: Feel free to add "visualize=True" parameter while debugging

        # Check for EF1
        self.assertTrue(ec_alloc.is_ef1(), "Envy-cycle elim. allocation should be EF1 for adventurers' nonadditive valuations")


if __name__ == '__main__':
    unittest.main()