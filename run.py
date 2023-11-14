import llm

from montecarlo.node import Node
from montecarlo.montecarlo import MonteCarlo

from lang import score_func, can_be_solution

from prompts import prompt, expansion_count, min_lines, check_fun

montecarlo = MonteCarlo(Node(prompt))

child_cache = {}

def generate_complete(text, montecarlo):
    text = llm.generate(text, 1)[0]
    score = score_func(text)
    if score is not None:
        if score < 0:
            return None
        else:
            if can_be_solution(text, min_lines, check_fun):
                montecarlo.solution = text
            return text
    else:
        return generate_complete(text, montecarlo)

def child_finder(node, montecarlo):
    text = generate_complete(node.state, montecarlo)
    if text is None:
        node.update_win_value(-1)
    else:
        cached_node = child_cache.get(text)
        if cached_node:
            current_node = cached_node

            while current_node.expanded:
                current_node = current_node.get_preferred_child(montecarlo.root_node)

            montecarlo.expand(current_node)
        else:
            child = Node(text)
            node.add_child(child)
            child.update_win_value(1)
            child.update_policy_value(1)

            child_cache[text] = child

            child = Node(node.state)
            node.add_child(child)
            child.update_policy_value(0.2)

montecarlo.child_finder = child_finder

montecarlo.simulate(expansion_count)

print('CHOSEN SOLUTION')
print(montecarlo.solution)
