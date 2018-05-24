#!/usr/bin/python2

# Stanford CS 109
# Problem Set 5, calculator

import csv
from scipy.special import binom as choose
from scipy.stats import binom, poisson, norm
from scipy.misc import factorial
from math import exp, sqrt
import random

def load_learning_outcomes():
    reader = csv.reader(open('learningOutcomes.csv'))
    learning_outcomes = []
    for row in reader:
        student_id = row[0]
        activity = row[1]
        outcome = float(row[2])
        learning_outcomes.append([student_id, activity, outcome])
    return learning_outcomes

def load_backgrounds(learning_outcomes):
    reader = csv.reader(open('background.csv'))
    index = 0
    for row in reader:
        experience = row[1]
        learning_outcomes[index].append(experience)
        index += 1
    return learning_outcomes

def part_a(learning_outcomes):
    sum_outcomes_act1 = 0.0
    sum_outcomes_act2 = 0.0
    num_students_act1 = 0
    num_students_act2 = 0
    for item in learning_outcomes:
        if item[1] == 'activity1':
            sum_outcomes_act1 += item[2]
            num_students_act1 += 1
        else:
            sum_outcomes_act2 += item[2]
            num_students_act2 += 1
    mean_act1 = sum_outcomes_act1 / num_students_act1
    mean_act2 = sum_outcomes_act2 / num_students_act2
    mean_diff = abs(mean_act2 - mean_act1)
    print("Activity 1: mean outcome is %.4g" %mean_act1)
    print("Activity 2: mean outcome is %.4g" %mean_act2)
    print("Difference of means: %.4g" %mean_diff)
    return mean_diff

def calc_p_value(outcome_subset, num_act1, num_act2, observed_diff):
    count_extreme = 0
    num_runs = 10000
    for i in range(num_runs):
        sum_outcomes_act1 = 0.0
        sum_outcomes_act2 = 0.0
        for j in range(num_act1):
            sum_outcomes_act1 += outcome_subset[random.randint(0, len(outcome_subset) - 1)][2]
        for k in range(num_act2):
            sum_outcomes_act2 += outcome_subset[random.randint(0, len(outcome_subset) - 1)][2]
        mean_act1 = sum_outcomes_act1 / num_act1
        mean_act2 = sum_outcomes_act2 / num_act2
        mean_diff = abs(mean_act1 - mean_act2)
        if mean_diff >= observed_diff:
            count_extreme += 1
    p_value = count_extreme * 1.0 / num_runs
    return p_value

def part_b(learning_outcomes, observed_diff):
    num_act1 = 0
    num_act2 = 0
    for item in learning_outcomes:
        if item[1] == 'activity1':
            num_act1 += 1
        else:
            num_act2 += 1
    p_value = calc_p_value(learning_outcomes, num_act1, num_act2, observed_diff)
    print("P-value is %.4g" %p_value)

def part_c(learning_outcomes):
    learning_outcomes = load_backgrounds(learning_outcomes)
    outcomes_more = []
    outcomes_avg = []
    outcomes_less = []
    sum_act1_more = 0.0
    sum_act2_more = 0.0
    sum_act1_avg = 0.0
    sum_act2_avg = 0.0
    sum_act1_less = 0.0
    sum_act2_less = 0.0
    num_act1_more = 0
    num_act2_more = 0
    num_act1_avg = 0
    num_act2_avg = 0
    num_act1_less = 0
    num_act2_less = 0
    for item in learning_outcomes:
        if item[3] == 'more':
            outcomes_more.append(item[0:3])
            if item[1] == 'activity1':
                sum_act1_more += item[2]
                num_act1_more += 1
            else:
                sum_act2_more += item[2]
                num_act2_more += 1
        elif item[3] == 'less':
            outcomes_less.append(item[0:3])
            if item[1] == 'activity1':
                sum_act1_less += item[2]
                num_act1_less += 1
            else:
                sum_act2_less += item[2]
                num_act2_less += 1
        else:
            outcomes_avg.append(item[0:3])
            if item[1] == 'activity1':
                sum_act1_avg += item[2]
                num_act1_avg += 1
            else:
                sum_act2_avg += item[2]
                num_act2_avg += 1
    mean_act1_more = sum_act1_more / num_act1_more
    mean_act2_more = sum_act2_more / num_act2_more
    mean_diff_more = abs(mean_act1_more - mean_act2_more)
    mean_act1_avg = sum_act1_avg / num_act1_avg
    mean_act2_avg = sum_act2_avg / num_act2_avg
    mean_diff_avg = abs(mean_act1_avg - mean_act2_avg)
    mean_act1_less = sum_act1_less / num_act1_less
    mean_act2_less = sum_act2_less / num_act2_less
    mean_diff_less = abs(mean_act1_less - mean_act2_less)
    p_value_more = calc_p_value(outcomes_more, num_act1_more, num_act2_more, mean_diff_more)
    p_value_avg = calc_p_value(outcomes_avg, num_act1_avg, num_act2_avg, mean_diff_avg)
    p_value_less = calc_p_value(outcomes_less, num_act1_less, num_act2_less, mean_diff_less)
    print("More experience")
    print("Activity 1: mean outcome is %.4g" %mean_act1_more)
    print("Activity 2: mean outcome is %.4g" %mean_act2_more)
    print("Difference of means: %.4g" %mean_diff_more)
    print("P-value is %.8g" %p_value_more)
    print("Average experience")
    print("Activity 1: mean outcome is %.4g" %mean_act1_avg)
    print("Activity 2: mean outcome is %.4g" %mean_act2_avg)
    print("Difference of means: %.4g" %mean_diff_avg)
    print("P-value is %.8g" %p_value_avg)
    print("Less experience")
    print("Activity 1: mean outcome is %.4g" %mean_act1_less)
    print("Activity 2: mean outcome is %.4g" %mean_act2_less)
    print("Difference of means: %.4g" %mean_diff_less)
    print("P-value is %.8g" %p_value_less)

def main():
    learning_outcomes = load_learning_outcomes()
    mean_diff = part_a(learning_outcomes)
    part_b(learning_outcomes, mean_diff)
    part_c(learning_outcomes)

if __name__ == '__main__':
    main()

