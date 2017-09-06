class Problem(object):
    """Representation of a problem"""

    def __init__(self, initial, goal):
        self.initial = list(initial)
        self.goal = list(goal)

    def actions(self, state):
        """Returns possible actions on current state"""
        actions_list = []
        index_of_blank_space = state.index("0")

        # The four possible actions Up, Down, Left and Right
        # can only be done if the blank space is in a certain space
        if index_of_blank_space == 0 or index_of_blank_space == 1 \
                or index_of_blank_space == 2:
            actions_list.append("Up")

        if index_of_blank_space == 3 or index_of_blank_space == 4 \
                or index_of_blank_space == 5:
            actions_list.append("Down")

        if index_of_blank_space == 0 or index_of_blank_space == 1 \
                or index_of_blank_space == 3 or index_of_blank_space == 4:
            actions_list.append("Left")

        if index_of_blank_space == 1 or index_of_blank_space == 2 \
                or index_of_blank_space == 4 or index_of_blank_space == 5:
            actions_list.append("Right")

        return actions_list

    def result(self, state, action):
        """Returns resulting state after a certain action"""
        # Has not taken in account false moves

        wState = list(state)

        index_of_blank_space = state.index("0")

        if action == "Left":
            wState[index_of_blank_space], wState[index_of_blank_space + 1] \
                = wState[index_of_blank_space + 1], wState[index_of_blank_space]

        if action == "Right":
            wState[index_of_blank_space], wState[index_of_blank_space - 1] \
                = wState[index_of_blank_space - 1], wState[index_of_blank_space]

        if action == "Up":
            wState[index_of_blank_space], wState[index_of_blank_space + 3] \
                = wState[index_of_blank_space + 3], wState[index_of_blank_space]

        if action == "Down":
            wState[index_of_blank_space], wState[index_of_blank_space - 3] \
                = wState[index_of_blank_space - 3], wState[index_of_blank_space]


        return wState

    def goal_test(self, state):
        """Returns boolean whether the goal state has been reached"""
        if state == self.goal:
            return True
        else:
            return False
