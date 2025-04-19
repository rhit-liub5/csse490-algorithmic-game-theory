class Agent:
    def __init__(self, name: str, valuation: dict):
        self.name = name
        self.valuation = valuation.copy()
        self.bundle = frozenset() # frozenset is immutable and hashable, so it can serve as a dictionary key


    def clear_bundle(self):
        self.bundle = frozenset()


    def add_to_bundle(self, item):
        self.bundle = frozenset(self.bundle.union(set([item])))


    def overwrite_bundle(self, new_bundle: frozenset):
        self.clear_bundle()
        for item in new_bundle:
            self.add_to_bundle(item)


    def envies(self, other: 'Agent'): # Curious why the Agent type hint is in quotes? See https://peps.python.org/pep-0484/#forward-references
        # TODO: Implement this method for Activity 1
        pass


    def envies_up_to_one(self, other: 'Agent'): # Curious why the Agent type hint is in quotes? See https://peps.python.org/pep-0484/#forward-references
        # TODO: Implement this method for Activity 1
        pass
    

    def get_value(self, bundle: frozenset): # frozenset is immutable and hashable, so it can serve as a dictionary key
        if bundle in self.valuation: 
            return self.valuation[bundle]
        
        # If bundle-specific value is not in valuation dictionary, 
        # default to additive valuation
        return sum([self.valuation[frozenset([item])] for item in bundle])


    def get_favorite(self, item_set: set):
        max_value = -1000
        favorite = None
        for item in item_set:
            item_value = self.get_value(frozenset([item]))
            if item_value > max_value:
                max_value = item_value
                favorite = item

        return favorite
    

    def __str__(self):
        return f"{type(self).__name__} named {self.name}"


class AdditiveAgent(Agent):
    def get_value(self, bundle: frozenset):
        return sum([self.valuation[frozenset([item])] for item in bundle])
    

if __name__ == '__main__':
    # Demonstrate Agent and AdditiveAgent classes
    first_valuation = {
        frozenset([1]): 5, 
        frozenset([2]): 4, 
        frozenset([3]): 3, 
        frozenset([1, 2]): 7
    }
    
    first_agent = Agent("Agent 1", first_valuation)
    print(first_agent)
    first_agent.add_to_bundle(1)
    print(first_agent.bundle, first_agent.get_value(first_agent.bundle))
    first_agent.add_to_bundle(2)
    print(first_agent.bundle, first_agent.get_value(first_agent.bundle))
    first_agent.clear_bundle()
    first_agent.add_to_bundle(3)
    print(first_agent.bundle, first_agent.get_value(first_agent.bundle))

    print()

    second_agent = AdditiveAgent("Agent 2", first_valuation)
    print(second_agent)
    second_agent.add_to_bundle(1)
    print(second_agent.bundle, second_agent.get_value(second_agent.bundle))
    second_agent.add_to_bundle(2)
    print(second_agent.bundle, second_agent.get_value(second_agent.bundle))
    second_agent.clear_bundle()
    second_agent.add_to_bundle(3)
    print(second_agent.bundle, second_agent.get_value(second_agent.bundle))