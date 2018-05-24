#!/usr/bin/python2

# Stanford CS 109
# Problem Set 1, Problem 13

import csv

def load_csv_data(filename):
    '''
    Reads in a 2D array of values separated by commas from a file.
    Parameter:
    filename -- name of file
    Return:
    2D array of float values
    '''
    matrix = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            float_row = []
            for value in row:
                float_row.append(float(value))
            matrix.append(float_row)
    return matrix

def print_data(matrix):
    '''
    Prints out a 2D array.
    Parameter:
    matrix -- 2D array
    '''
    for row in matrix:
        print row

def calc_loc_probs(prior, cond):
    '''
    Calculates the probability that the phone is at a location given
    the prior location probability and the conditional probability that
    a signal is observed if the phone is at that location.
    Uses Bayes' Theorem.
    Parameters:
    prior -- 2D array of prior location probabilities
    cond -- 2D array of conditional probabilities
    Result:
    2D array of probabilities that the phone is at a location if the
    signal is observed
    '''
    norm_const = 0.0
    for row in range(0, len(prior)):
        for col in range(0, len(prior[0])):
            norm_const += prior[row][col]
    result = []
    for row in range(0, len(prior)):
        result_row = []
        for col in range(0, len(prior[0])):
            loc_prob = prior[row][col] * cond[row][col] / norm_const
            result_row.append(loc_prob)
        result.append(result_row)
    return result

def main():
    prior = load_csv_data('prior.csv')
    cond = load_csv_data('conditional.csv')
    print("P(location):")
    print_data(prior)
    print
    print("P(observe signal | location):")
    print_data(cond)
    print
    result = calc_loc_probs(prior, cond)
    print("P(location | observe signal):")
    print_data(result)

if __name__ == '__main__':
    main()

