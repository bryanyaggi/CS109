#!/usr/bin/python2

# Stanford CS 109
# Problem Set 6, calculator

from scipy.special import binom as choose
from scipy.stats import binom, poisson, norm
from scipy.misc import factorial
from math import exp, sqrt

def p1():
    mu_pA = 20.0 * 50
    sigma_pA = sqrt(20.0 * 100)
    Y_pA = norm(mu_pA, sigma_pA)
    print("P(Y_pA < 950) = %.4g" %Y_pA.cdf(950))
    mu_pB = 20 * 52
    sigma_pB = sqrt(20.0 * 200)
    Y_pB = norm(mu_pB, sigma_pB)
    print("P(Y_pB < 950) = %.4g" %Y_pB.cdf(950))
    mu_diff = mu_pB - mu_pA
    sigma_diff = sqrt(sigma_pB ** 2 - sigma_pA ** 2)
    Y_diff = norm(mu_diff, sigma_diff)
    print("P(Y_pA - Y_pB <= 0) = %.4g" %Y_diff.cdf(0))

def p2():
    mu_X = 7.0 / 2
    var_X = 35.0 / 12
    sigma_X = sqrt(var_X)
    n = 30
    mu_Y = n * mu_X
    sigma_Y = sqrt(n * var_X)
    Y = norm(mu_Y, sigma_Y)
    print("P(Y <= 100) = %.4g" %Y.cdf(100))

def p3():
    val = (4.0 * norm.ppf(.95)) ** 2
    print("n >= %.4g" %val)

def print_p1():
    p1()

def print_p2():
    p2()

def print_p3():
    p3()

def main():
    #print_p1()
    #print_p2()
    print_p3()

if __name__ == '__main__':
    main()

