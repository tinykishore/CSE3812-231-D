# Importing the random module
import random


# Function for initializing the state and return with 10 random values
def initialize_state():
    # return a list of 10 random values between 0 and 20
    return random.sample(range(-20, 20), 10)


# Function for calculating the cost of the state
# It will return the cost (number of values that are not in order)
def calc_cost(_state_: list):
    # Initializing the local cost variable
    _cost_ = 0
    # Calculating the cost with nested for loop
    for i in range(len(_state_)):
        for j in range(i + 1, len(_state_)):
            # If the value at index i is greater than the value at index j,
            # then increment the cost
            # Determine total misplaced values
            if _state_[i] > _state_[j]:
                _cost_ += 1
    return _cost_


# Algorithm for hill climbing with the steepest ascent
# Function for generating the next state
# It will return the next state and the cost of the next state
def state_generator_steepest_ascent(_state_: list):
    # Initializing the local current cost variable
    current_cost = calc_cost(_state_)

    # Generating the next state with nested for loop
    for i in range(len(_state_)):
        for j in range(i + 1, len(_state_)):
            # Swap the values at index i and j and store the cost of the new state
            swap(_state_, i, j)
            new_cost = calc_cost(_state_)

            # If the new cost is less than the current cost, then update the current cost
            # otherwise, swap the values back
            if new_cost < current_cost:
                current_cost = new_cost
            else:
                swap(_state_, i, j)
    # Return the next state and the cost of the next state
    return _state_, current_cost


# Function for swapping two values in a list
def swap(_state_: list, i: int, j: int):
    _state_[i], _state_[j] = _state_[j], _state_[i]


# Function for testing if the state is the goal state
def goal_test(_state_):
    # Return True if the cost of the state is 0
    return calc_cost(_state_) == 0


# Main function
if __name__ == '__main__':
    # Initializing the state
    state = initialize_state()

    # Printing the initial state
    print('Initial State: \t', state)

    # Performing hill climbing with the steepest ascent, until the goal state is reached
    while not goal_test(state):
        state, cost = state_generator_steepest_ascent(state)

    # Printing the goal state
    print('Goal State: \t', state)
