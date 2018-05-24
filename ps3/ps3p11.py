#!/usr/bin/python2

# Stanford CS 109
# Problem Set 3, Problem 11

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom

def get_sent_lengths(filename):
    sent_lengths = {}
    with open(filename) as infile:
        for line in infile:
            words = line.split()
            num_words = len(words)
            if num_words in sent_lengths:
                sent_lengths[num_words] += 1
            else:
                sent_lengths[num_words] = 1
    return sent_lengths

def plot_sent_length_pmf(sent_lengths):
    num_sents = 0
    for key in sent_lengths:
        num_sents += sent_lengths[key]
    pmf_x_vals = []
    pmf_y_vals = []
    for i in range(1, 11):
        pmf_x_vals.append(i)
        if i in sent_lengths.keys():
            pmf_y_vals.append(float(sent_lengths[i]) / num_sents)
        else:
            pmf_y_vals.append(0)
    plt.title('PMF of Sentence Lengths in Moby Dick')
    plt.xlabel('Sentence Length [words]')
    plt.ylabel('Probability')
    plt.xticks(np.arange(min(pmf_x_vals), max(pmf_x_vals) + 1, 1))
    plt.bar(pmf_x_vals, pmf_y_vals)
    plt.savefig('ps3p11a.png')
    plt.show()

def plot_geo_pmf():
    p = .04
    X = geom(p)
    pmf_x_vals = []
    pmf_y_vals = []
    for i in range(1, 11):
        pmf_x_vals.append(i)
        pmf_y_vals.append(X.pmf(i))
    plt.title('PMF of Geo(0.04)')
    plt.xlabel('Sentence Length [words]')
    plt.ylabel('Probability')
    plt.xticks(np.arange(min(pmf_x_vals), max(pmf_x_vals) + 1, 1))
    plt.bar(pmf_x_vals, pmf_y_vals)
    plt.savefig('ps3p11c.png')
    plt.show()

def main():
    sent_lengths = get_sent_lengths('moby-dick.txt')
    plot_sent_length_pmf(sent_lengths)
    plot_geo_pmf()

if __name__ == '__main__':
    main()

