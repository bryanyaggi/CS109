#!/usr/bin/python2

# Stanford CS 109
# Problem Set 4, calculator

from scipy.special import binom as choose
from scipy.stats import binom, poisson, norm
from scipy.misc import factorial
from math import exp, sqrt

def p1():
    rate_1 = 7.5
    X_1 = poisson(rate_1)
    print("P(X_1 > 10) = %.4g" %(1 - X_1.cdf(10)))
    # Check calculation.
    p_a_c = 0.0
    for i in range(0, 11):
        p_a_c += rate_1 ** i / (factorial(i)) * exp(-rate_1)
    #print(1 - p_a_c)

    X_2 = poisson(2 * rate_1)
    print("P(X_2 > 15) = %.4g" %(1 - X_2.cdf(15)))

    X_3 = poisson(3 * rate_1)
    print("P(X_3 > 20) = %.4g" %(1 - X_3.cdf(20)))

def p4(sigma):
    mu = 6
    X = norm(mu, sigma)
    print("P(X <= 9) = %.4g" %(X.cdf(9)))
    print("P(X > 9) = %.4g" %(1 - X.cdf(9)))

def p6():
    mu = 2200
    sigma = sqrt(52900)
    Y = norm(2 * mu, 2 * sigma)
    print("P(Y > 5000) = %.4g" %(1 - Y.cdf(5000)))
    X = norm(mu, sigma)
    P_Xl2000 = X.cdf(2000)
    P_Xg2000 = 1 - P_Xl2000
    P_Z2 = choose(3, 2) * (P_Xg2000 ** 2) * P_Xl2000
    P_Z3 = P_Xg2000 ** 3
    print("P(X > 2000) = %.4g" %P_Xg2000)
    print("P(X <= 2000) = %.4g" %P_Xl2000)
    print("P(Z_2) = %.4g" %P_Z2)
    print("P(Z_3) = %.4g" %P_Z3)
    print("P(Z_2 or Z_3) = %.4g" %(P_Z2 + P_Z3))

def calc_run_prob(sequence):
    num_runs = 0
    num_H = 0
    num_T = 0
    prev_val = 'N'
    for i in range(0, len(sequence)):
        if sequence[i] != prev_val:
            num_runs += 1
            prev_val = sequence[i]
        if sequence[i] == 'H':
            num_H += 1
        else:
            num_T += 1
    print("  runs: %d" %num_runs)
    print("  H: %d" %num_H)
    print("  T: %d" %num_T)
    P = 0
    if num_runs % 2 == 0:
        k = num_runs/2
        P = 2*choose(num_H-1,k-1)*choose(num_T-1,k-1)/choose(num_H+num_T,num_H)
    else:
        k = (num_runs-1)/2
        P = (choose(num_H-1,k)*choose(num_T-1,k-1)+choose(num_T-1,k)*choose(num_H-1,k-1))/choose(num_H+num_T,num_H)
    print("  P = %.4g" %P)

def p11():
    sequence_1 = '''TTHHTHTTHTTTHTTTHTTTHTTHTHHTHHTHTHHTTTHHTHTHTTHTHH
                    TTHTHHTHTTTHHTTHHTTHHHTHHTHTTHTHTTHHTHHHTTHTHTTTHH
                    TTHTHTHTHTHTTHTHTHHHTTHTHTHHTHHHTHTHTTHTTHHTHTHTHT
                    THHTTHTHTTHHHTHTHTHTTHTTHHTTHTHHTHHHTTHHTHTTHTHTHT
                    HTHTHTHHHTHTHTHTHHTHHTHTHTTHTTTHHTHTTTHTHHTHHHHTTT
                    HHTHTHTHTHHHTTHHTHTTTHTHHTHTHTHHTHTTHTTHTHHTHTHTTT'''
    sequence_2 = '''HTHHHTHTTHHTTTTTTTTHHHTTTHHTTTTHHTTHHHTTHTHTTTTTTH
                    THTTTTHHHHTHTHTTHTTTHTTHTTTTHTHHTHHHHTTTTTHHHHTHHH
                    TTTTHTHTTHHHHTHHHHHHHHTTHHTHHTHHHHHHHTTHTHTTTHHTTT
                    THTHHTTHTTHTHTHTTHHHHHTTHTTTHTHTHHTTTTHTTTTTHHTHTH
                    HHHTTTTHTHHHTHHTHTHTHTHHHTHTTHHHTHHHHHHTHHHTHTTTHH
                    HTTTHHTHTTHHTHHHTHTTHTTHTTTHHTHTHTTTTHTHTHTTHTHTHT'''
    sequence_3 = "HTHHTT"
    print("Sequence 1:")
    calc_run_prob(sequence_1)
    print("Sequence 2:")
    calc_run_prob(sequence_2)
    print("Sequence 3:")
    calc_run_prob(sequence_3)

def print_p1():
    p1()

def print_p4():
    sigma = 5.75
    p4(sigma)
    print("Var(X) = %.4g" %(sigma ** 2))

def print_p6():
    p6()

def print_p11():
    p11()

def main():
    #print_p1()
    #print_p4()
    #print_p6()
    print_p11()

if __name__ == '__main__':
    main()

