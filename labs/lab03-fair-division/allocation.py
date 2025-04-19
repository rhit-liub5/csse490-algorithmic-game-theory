from agent import Agent
from typing import Callable


class Allocation:
    def __init__(self, num_items: int, agents: list[Agent], proc: Callable):
        self.num_items = num_items
        self.agents = agents.copy()
        self.proc = proc
    

    def allocate(self, visualize=False):
        for agent in self.agents:
            agent.clear_bundle()
        
        self.proc(self.num_items, self.agents, visualize=visualize)

    
    def get_unallocated_items(self):
        all_items = set([i for i in range(1, self.num_items + 1)])
        allocated_items = set()
        for agent in self.agents:
            allocated_items = allocated_items.union(agent.bundle)
        return all_items.difference(allocated_items)

    
    def is_ef1(self):
        remaining_items = self.get_unallocated_items()
        if remaining_items:
            print("Warning: Called is_ef1 with some items still unallocated.")
        
        # TODO: Finish implementing this function for Activity 1
        
        return True
    

    def is_prop1(self):
        remaining_items = self.get_unallocated_items()
        if remaining_items:
            print("Warning: Called is_ef1 with some items still unallocated.")

        grand_bundle = frozenset([i for i in range(1, self.num_items + 1)])
        for agent in self.agents:
            is_prop1 = False
            prop_value = agent.get_value(grand_bundle) * 1. / len(self.agents)
            
            # TODO: Finish implementing this function for Activity 1
            
            if not is_prop1:
                print(f"Not PROP1: {agent.name} received value {agent.get_value(agent.bundle)}, prop_value is {prop_value}, and no outside item bridges the gap.")
                return False
        
        return True


    def __str__(self):
        str_rep = f"Allocation with {self.num_items} items to {len(self.agents)} agents using {self.proc.__name__} procedure.\n"
        for agent in self.agents:
            str_rep += f"\t{agent} receives bundle {agent.bundle}\n"
        return str_rep
