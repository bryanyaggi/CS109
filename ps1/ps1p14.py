#!/usr/bin/python2

# Stanford CS 109
# Problem Set 1, Problem 14, Part b

import random

def simulation(num_trials = 100000):
    num_events = 0
    
    for trial in range(0, num_trials):
        first_int = random.randint(1, 12)
        second_int = random.randint(1, 12)
        if second_int > first_int:
            num_events = num_events + 1

    return num_events * 1.0 / num_trials


if __name__ == '__main__':
    print(simulation())

