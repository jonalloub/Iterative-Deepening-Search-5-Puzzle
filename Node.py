from Problem import Problem

class Node(object):
    def __init__(self, state, parent=None, action=None):
        self.action = action
        self.state = list(state)
        self.parent = parent

    def __repr__(self):
        return "Node {}".format(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, self, action)

    def solution(self):
        """Returns the solution, the sequence of actions it took to get to this node"""

        node, path_back = self, []

        while node:
            path_back.append(node.action)
            node = node.parent

        return list(reversed(path_back))



