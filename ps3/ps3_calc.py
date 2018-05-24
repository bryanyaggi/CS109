#!/usr/bin/python2

# Stanford CS 109
# Problem Set 3, calculator

from scipy.special import binom as choose
from scipy.stats import binom, poisson
from scipy.misc import factorial
from math import exp

def p3(X):
    p = 0.5

    N_max = 0
    i = 0
    while 2 ** i < X:
        i += 1
        N_max = i

    P_NgeX = p ** N_max
    E_W = 0.0

    for N in range(0, N_max + 1):
        if N == N_max:
            E_W += X * P_NgeX
        else:
            E_W += (2.0 ** N) * (p ** (N + 1))

    return E_W

def p4():
    print("key tests")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for key in range(1, 11):
        num_eqtest = 0
        low = 0
        high = 9
        while low <= high:
            mid = (low + high) / 2
            num_eqtest += 1
            if key == arr[mid]:
                break
            elif key > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        print("%3d %5d" %(key, num_eqtest))

def p6():
    p_wrong_g = 0.25
    p_wrong_i = 0.15
    P_guilty = 0.7
    P_innocent = 1 - P_guilty
    P_conv_g = 0.0
    P_conv_i = 0.0
    for i in range(9, 13):
        P_conv_g += choose(12, i) * ((1 - p_wrong_g) ** i) * (p_wrong_g ** (12 - i))
        P_conv_i += choose(12, i) * (p_wrong_i ** i) * ((1 - p_wrong_i) ** (12 - i))
    print("P_conv_g = %.4g" %P_conv_g)
    print("P_conv_i = %.4g" %P_conv_i)
    P_correct = P_conv_g * P_guilty + (1 - P_conv_i) * P_innocent
    P_convicted = P_conv_g * P_guilty + P_conv_i * P_innocent
    print("P_correct = %.4g" %P_correct)
    print("P_convicted = %.4g" %P_convicted)

def p7():
    n = 2000
    m = 10000
    lam = m / n
    P_leq8 = 0.0
    for i in range(0, 9):
        P_leq8 += (float (lam ** i) / factorial(i) * exp(-lam))
    print("P(X <= 8) = %.3f" %P_leq8)

def p8():
    num_servers = 100
    lam = 2
    p_ncs = 0.0
    for i in range(0, 6):
        p_ncs += (float (lam ** i) / factorial(i) * exp(-lam))
    p_ncdc = p_ncs ** num_servers
    print("P(single server will crash) = %f" %(1 - p_ncs))
    print("P(no server crash in data center) = %f" %p_ncdc)

def p10():
    N = 5000
    p_A = .51
    X = binom(N, p_A)
    Y = poisson(N * p_A)
    P_Awins_bin = 1 - X.cdf(N/2)
    P_Awins_poi = 1 - Y.cdf(N/2)
    print("P(A wins) using binomial distribution = %f" %P_Awins_bin)
    print("P(A wins) using poisson distribution = %f" %P_Awins_poi)

def print_p3():
    print("X = $20: E[W] = %.3f" %p3(20))
    print("X = $500: E[W] = %.3f" %p3(500))
    print("X = $10000: E[W] = %.3f" %p3(10000))

def print_p4():
    p4()

def print_p6():
    p6()

def print_p7():
    p7()

def print_p8():
    p8()

def print_p10():
    p10()

def main():
    #print_p3()
    #print_p4()
    #print_p6()
    #print_p7()
    #print_p8()
    print_p10()

if __name__ == '__main__':
    main()

