#!/usr/bin/python2

# Stanford CS 109
# Problem Set 6, Problem 6

# Naive Bayes Classifier for Binary Data Sets

from collections import namedtuple
from numpy import log

'''
Named tuple used to store data vectors
'''
vector = namedtuple('vector', 'inputs output')

def load_vectors(filename):
    '''
    Reads in data vectors from a file and returns them as a list of vector
    tuples.
    
    Parameter:
    filename -- name of data file
    File format error checking is not implemented. The file format should be as
    follows.

    <BOF>
    <number of input variables per vector>
    <number of data vectors in file>
    <first data vector>
    ...
    <nth data vector>
    <EOF>

    Each vector should be formatted as follows.

    <input_1> <input_2> ... <input_n>: output

    Return:
    list containing vector tuples

    '''
    with open(filename) as infile:
        num_inputs = int(next(infile))
        num_vectors = int(next(infile))
        vectors = []
        for line in infile:
            inputs = []
            for i in range(num_inputs):
                inputs.append(int(line[i * 2]))
            output = int(line[num_inputs * 2 + 1])
            vectors.append(vector(inputs, output))
    infile.close()
    return vectors

def train_count(vectors):
    '''
    Takes training vectors, counts the number of occurrances of the input
    variable value and output value combination for each input variable, and
    returns these counts in a multidimensional list.

    Parameter:
    vectors -- list containing training data vector tuples

    Return:
    multidimensional list containing counts of each input, output combnation

    counts = [[[<counts output=0 and input_1=0>, <counts output=0 and input_1=1>],
    [<counts output=1 and input_1=0>, <counts output=1 and input_1=1>]], ... ,
    [[<counts output=0 and input_n=0>, <counts output=0 and input_n=1>],
    [<counts output=1 and input_n=0>, <counts output=1 and input_n=1>]]]
    '''
    counts = []
    # Initialize counts
    for i in range(len(vectors[0].inputs)):
        count = []
        count.append([0, 0])
        count.append([0, 0])
        counts.append(count)
    # Count occurrances
    for vect in vectors:
        y = vect.output
        index = 0
        for x in vect.inputs:
            counts[index][y][x] += 1
            index += 1
    return counts

def print_results(num_out_0_tested, num_out_1_tested, num_out_0_correct,
        num_out_1_correct):
    '''
    Prints results of test.

    Parameters:
    num_out_0_tested -- integer number of vectors tested with output = 0
    num_out_1_tested -- integer number of vectors tested with output = 1
    num_out_0_correct -- integer number of vectors predicted correctly with
        output = 0
    num_out_1_correct -- integer number of vectors predicted correctly with
        output = 1
    '''
    total_tested = num_out_0_tested + num_out_1_tested
    total_correct = num_out_0_correct + num_out_1_correct
    print("Class 0: tested %d, correctly classified %d" %(num_out_0_tested,
        num_out_0_correct))
    print("Class 1: tested %d, correctly classified %d" %(num_out_1_tested,
        num_out_1_correct))
    print("Overall: tested %d, correctly classified %d" %(total_tested,
        total_correct))
    print("Accuracy: %.3g" %(1.0 * total_correct / total_tested))

def test_mle(counts, vectors):
    '''
    Uses maximum likelihood estimation on training data to predict outputs
    for new data vectors.

    MLE is computed as follows.
    p(input=x|output=y) = <num examples input=x and output=y>/<num examples output=y>

    The output is predicted using Naive Bayes. The output that maximizes the
    log of the Naive Bayes assumption is chosen.

    Parameters:
    counts -- multidimensional list containing counts of each input, output
    combination
    vectors -- list containing test data vector tuples
    '''
    probs = [] # multidimensional list for storing conditional probabilities
    count_y = [0, 0] # for counting occurances of each output
    for count in counts:
        prob = []
        for i in range(2):
            denom = 1.0 * count[i][0] + count[i][1]
            prob.append([count[i][0] / denom, count[i][1] / denom])
            count_y[i] += (count[i][0] + count[i][1])
        probs.append(prob)
    denom = 1.0 * count_y[0] + count_y[1]
    prob_y = [count_y[0] / denom, count_y[1] / denom] # probability of each output
    num_out_0_tested = 0
    num_out_1_tested = 0
    num_out_0_correct = 0
    num_out_1_correct = 0
    # Compute log probability of each output
    for vect in vectors:
        p_0 = log(prob_y[0])
        p_1 = log(prob_y[1])
        index = 0
        for inp in vect.inputs:
            if probs[index][0][inp] == 0: # check before taking log(0)
                p_0 += float('-inf')
            else:
                p_0 += log(probs[index][0][inp])
            if probs[index][1][inp] == 0: # check before taking log(0)
                p_1 += float('-inf')
            else:
                p_1 += log(probs[index][1][inp])
            index += 1
        output = 0
        if p_1 > p_0:
            output = 1
        if vect.output == 0:
            num_out_0_tested += 1
            if output == 0:
                num_out_0_correct += 1
        else:
            num_out_1_tested += 1
            if output == 1:
                num_out_1_correct += 1
    total_tested = num_out_0_tested + num_out_1_tested
    total_correct = num_out_0_correct + num_out_1_correct
    print("MLE Result...")
    print_results(num_out_0_tested, num_out_1_tested, num_out_0_correct,
            num_out_1_correct)

def test_laplace(counts, vectors):
    '''
    Uses maximum likelihood estimation with Laplace smoothing on training data
    to predict outputs for new data vectors.

    MLE with Laplace smoothing is computed as follows.
    p(input=x|output=y) = (<num examples input=x and output=y> + 1)/(<num examples output=y> + 2)

    The output is predicted using Naive Bayes. The output that maximizes the
    log of the Naive Bayes assumption is chosen.

    Parameters:
    counts -- multidimensional list containing counts of each input, output
    combination
    vectors -- list containing test data vector tuples
    '''
    probs = []
    count_y = [0, 0]
    for count in counts:
        prob = []
        for i in range(2):
            denom = 1.0 * (count[i][0] + 1) + (count[i][1] + 1)
            prob.append([(count[i][0] + 1) / denom, (count[i][1] + 1) / denom])
            count_y[i] += (count[i][0] + count[i][1])
        probs.append(prob)
    denom = 1.0 * count_y[0] + count_y[1]
    prob_y = [count_y[0] / denom, count_y[1] / denom]
    num_out_0_tested = 0
    num_out_1_tested = 0
    num_out_0_correct = 0
    num_out_1_correct = 0
    for vect in vectors:
        p_0 = log(prob_y[0])
        p_1 = log(prob_y[1])
        index = 0
        for inp in vect.inputs:
            p_0 += log(probs[index][0][inp])
            p_1 += log(probs[index][1][inp])
            index += 1
        output = 0
        if p_1 > p_0:
            output = 1
        if vect.output == 0:
            num_out_0_tested += 1
            if output == 0:
                num_out_0_correct += 1
        else:
            num_out_1_tested += 1
            if output == 1:
                num_out_1_correct += 1
    total_tested = num_out_0_tested + num_out_1_tested
    total_correct = num_out_0_correct + num_out_1_correct
    print("Laplace Smoothing Result...")
    print_results(num_out_0_tested, num_out_1_tested, num_out_0_correct,
            num_out_1_correct)

def train_and_test(train_filename, test_filename):
    '''
    Runs the functions required to create a Naive Bayes classifier and test
    a new dataset.

    Parameters:
    train_filename -- filename for training data
    test_filename -- filename for testing data
    '''
    train_vectors = load_vectors(train_filename)
    counts = train_count(train_vectors)
    test_vectors = load_vectors(test_filename)
    test_mle(counts, test_vectors)
    test_laplace(counts, test_vectors)

def main():
    print("Simple")
    train_and_test('simple-train.txt', 'simple-test.txt')

    print("")
    print("US Representative Party Affiliation")
    train_and_test('vote-train.txt', 'vote-test.txt')

    print("")
    print("Heart Disease")
    train_and_test('heart-train.txt', 'heart-test.txt')

if __name__ == '__main__':
    main()

