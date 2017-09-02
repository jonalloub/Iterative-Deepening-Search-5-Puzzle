class Problem(object):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        actions_list = []
        index_of_blank_space = state.index("0")

        # The four possible actions Up, Down, Left and Right
        # can only be done if the blank space is in a certain space
        if index_of_blank_space == 0 or index_of_blank_space == 1 \
                or index_of_blank_space == 2:
            actions_list.append("Up")

        if index_of_blank_space == 3 or index_of_blank_space == 5 \
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
        # Has not taken in account false moves

        index_of_blank_space = state.index("0")

        if action == "Left":
            state[index_of_blank_space], state[index_of_blank_space + 1] \
                = state[index_of_blank_space + 1], state[index_of_blank_space]

        if action == "Right":
            state[index_of_blank_space], state[index_of_blank_space - 1] \
                = state[index_of_blank_space - 1], state[index_of_blank_space]

        if action == "Up":
            state[index_of_blank_space], state[index_of_blank_space + 3] \
                = state[index_of_blank_space + 3], state[index_of_blank_space]

        if action == "Down":
            state[index_of_blank_space], state[index_of_blank_space - 3] \
                = state[index_of_blank_space - 3], state[index_of_blank_space]

        return state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False



# Brief tests

initial = ['1', '2', '3', '0', '4', '5']
goal = ['0', '1', '2', '3', '4', '5']
trial = Problem(initial, goal)

print(trial.actions(initial))
print(trial.result(initial, "Left"))
print(trial.goal_test(goal))