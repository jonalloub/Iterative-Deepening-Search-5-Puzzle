from Node import Node
from Problem import Problem
import sys

def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result



def depth_limited_search(problem, limit = 200 ):
    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return "cutoff"
        else:
            cutoff = False
            for child in node.expand(problem):
                print("Child: " + str(child))
                print("Parent: " + str(child.parent))
                print("Problem: " + str(problem.initial))
                result = recursive_dls(child, problem, limit - 1)
                if result == "cutoff":
                    cutoff = True
                elif result is not None:
                    return result
            return "cutoff" if cutoff else None

    return recursive_dls(Node(problem.initial), problem, limit)

initial = ["4", "3","1","5","0","2"]
goal = ["1", "2","3","4","5","0"]
problem = Problem(initial, goal)
print(iterative_deepening_search(problem))
