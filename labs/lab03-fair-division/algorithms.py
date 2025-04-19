from agent import Agent, AdditiveAgent
from allocation import Allocation
import matplotlib.pyplot as plt
import networkx as nx
import random


def round_robin(num_items: int, agents: list[Agent], shuffle=False, visualize=False) -> None:
    """
    Round-robin allocation of items to agents.
    Modifies agents' bundles directly, so there is no returned value. 
    """
    if shuffle:
        print([agent.name for agent in agents])
        random.shuffle(agents)
        print([agent.name for agent in agents])

    # TODO: Finish implementing this function for Activity 2. 
    # If the visualize flag is set to True, you should call the draw_envy_graph function at appropriate times. 
    raise NotImplementedError("Round-robin allocation not implemented yet.")


def random_allocation(num_items: int, agents: list[Agent], shuffle=False, visualize=False) -> None:
    """
    Random allocation of items to agents, 
    included as an example of how to allocate items. 
    """
    if shuffle:
        print([agent.name for agent in agents])
        random.shuffle(agents)
        print([agent.name for agent in agents])

    for i in range(1, num_items + 1):
        random.choice(agents).add_to_bundle(i)
    return


def envy_cycle_elimination(num_items: int, agents: list[Agent], shuffle=False, visualize=False) -> None:
    if shuffle:
        print([agent.name for agent in agents])
        random.shuffle(agents)
        print([agent.name for agent in agents])
    
    # TODO: Finish implementing this function for Activity 3. 
    # If the visualize flag is set to True, you should call the draw_envy_graph function at appropriate times. 
    raise NotImplementedError("Envy cycle elimination not implemented yet.")


def construct_envy_graph(agents: list[Agent]):
    """
    DO NOT MODIFY! 
    Construct the (directed) envy graph for the given set of agents 
    as a NetworkX DiGraph. 
    """
    G = nx.DiGraph()

    for agent in agents:
        G.add_node(agent.name, agent=agent)

    for agent in agents:
        for other in agents:
            if agent.envies(other):
                G.add_edge(agent.name, other.name)
    return G


def draw_envy_graph(envy_graph: nx.DiGraph):
    """
    DO NOT MODIFY! 
    Plot the given envy graph using matplotlib. 
    Node labels are the last "pieces" of agent names (after the last space, if any). 
    DO NOT MODIFY! 
    """
    pos = nx.spring_layout(envy_graph)
    nx.draw_networkx_nodes(envy_graph, pos, node_size=500)
    nx.draw_networkx_edges(envy_graph, pos, arrows=True, arrowstyle='-|>', arrowsize=20)
    label_map = {node: envy_graph.nodes[node]['agent'].name.split(' ')[-1] for node in envy_graph.nodes}
    nx.draw_networkx_labels(envy_graph, pos, labels=label_map)
    plt.axis('off')
    plt.show()
    return


def eliminate_cycle(G: nx.DiGraph, visualize=False):
    cycle = nx.find_cycle(G, orientation='original') # returns list of directed edges
    if visualize:
        print(f"*** Found cycle: {cycle} ***")

    # TODO: Finish implementing this function for Activity 3
    raise NotImplementedError("Cycle elimination not implemented yet.")


def summarize_agent_bundles(agents: list[Agent]):
    """
    DO NOT MODIFY! 
    Prints a summary of agents' current bundles. 
    Use this for debugging as needed. 
    """
    for agent in agents:
        print(f"\t{str(agent)} has bundle {agent.bundle}")


if __name__ == '__main__': 
    # TODO: Feel free to add your own examples here for testing, 
    # or add to the provided test cases in tests.py.
    
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
    print(f"Is round-robin allocation EF1? {'yes' if rr_alloc.is_ef1() else 'no'}")
    print(f"Is round-robin allocation PROP1? {'yes' if rr_alloc.is_prop1() else 'no'}")

    ec_alloc = Allocation(num_items=5, agents=[agent_one, agent_two, agent_three], proc=envy_cycle_elimination)
    ec_alloc.allocate(visualize=True)
    print(f"Is envy cycle allocation EF1? {'yes' if ec_alloc.is_ef1() else 'no'}")
    print(f"Is envy cycle allocation PROP1? {'yes' if ec_alloc.is_prop1() else 'no'}")
