import random
import numpy as np


def is_state_terminal(position, rewards):
    if rewards[position] == -1:
        return False
    else:
        return True


def get_next_state(exploration_rate, current_move):
    if exploration_rate < random.random():
        return np.argmax(current_move)
    else:
        return random.randint(0, 3)


def get_next_move(state, current_position, size):
    if state == 0 and current_position % size != 0:
        current_position -= 1
    if state == 1 and current_position // size != size - 1:
        current_position += size
    if state == 2 and current_position // size != 0:
        current_position -= size
    if state == 3 and current_position % size != size - 1:
        current_position += 1
    return current_position


def reward_table_initialize(maze, size, finish):
    rewards = []
    for row in maze:
        for field in row:
            if field == 'x':
                rewards.append(-(size ** 2))
            else:
                rewards.append(-1)
    rewards[finish] = size ** 2
    return rewards


def current_learned_path(start, rewards, q_table, size):
    path = []
    current_position = start
    path.append(current_position)
    moves = 0
    while not is_state_terminal(current_position, rewards) and moves < size ** 2:
        state = get_next_state(0, q_table[current_position])
        current_position = get_next_move(state, current_position, size)
        path.append(current_position)
        moves += 1
    return path


def q_learning(maze, size, start, finish,
               learning_rate, discount_rate, exploration_rate, min_exploration_rate, exploration_decrease, iterations):
    q_table = [[0 for _ in range(4)] for __ in range(size ** 2)]
    rewards = reward_table_initialize(maze, size, finish)

    for iteration in range(iterations):
        moves = 0
        current_position = start
        while not is_state_terminal(current_position, rewards) and moves < size ** 2:
            state = get_next_state(exploration_rate, q_table[current_position])
            next_move = get_next_move(state, current_position, size)
            reward = rewards[next_move]
            if current_position == next_move:
                reward -= 10
            old_value = (1 - learning_rate) * q_table[current_position][state]
            new_value = learning_rate * (reward + discount_rate * max(q_table[next_move]))
            q_table[current_position][state] = old_value + new_value

            current_position = next_move
            moves += 1
        if exploration_rate > min_exploration_rate:
            exploration_rate -= exploration_decrease

    path = current_learned_path(start, rewards, q_table, size)
    return path
