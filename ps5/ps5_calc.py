#!/usr/bin/python2

# Stanford CS 109
# Problem Set 5, calculator

from scipy.special import binom as choose
from scipy.stats import binom, poisson, norm
from scipy.misc import factorial
from math import exp, sqrt

def p2():
    p_pc = .4
    p_mac = .3
    p_linux = .1
    p_none = .2
    n_pc = 6
    n_mac = 4
    n_linux = 2
    n_none = 3
    P = factorial(15)/(factorial(n_pc) * factorial(n_mac) * factorial(n_linux) * factorial(n_none)) * (p_pc ** n_pc) * (p_mac ** n_mac) * (p_linux ** n_linux) * (p_none ** n_none)
    print("P = %.4g" %P)

def P_YisI(i):
    P_XisX = .2
    P = 0.0
    for x in range(1, 6):
        if x >= i:
            P += (P_XisX * 1 / x)
    return P

def p4():
    for i in range(1, 6):
        print("P(Y = %d) = %.4g" %(i, P_YisI(i)))

    for i in range(1, 6):
        print("P(X = x | Y = %d) = %.4g * 1/x" %(i, 1 / (5*P_YisI(i))))

def p5():
    E_X = 0.0
    E_Y = 0.0
    E_XY = 0.0
    p_roll = 1.0/6
    for i in range(1, 7):
        E_X += i * p_roll
        E_Y += i ** 2 * p_roll
        E_XY += i ** 3 * p_roll
    print("E[X] = %.4g" %E_X)
    print("E[Y] = %.4g" %E_Y)
    print("E[XY] = %.4g" %E_XY)
    print("Cov(X, Y) = %.4g" %(E_XY - E_X * E_Y))

def p_Y(Y, p_phone_a, p_phone_b, p_drop_a, p_drop_b):
    p_Y_a = p_phone_a * choose(3, Y) * (p_drop_a ** Y) * ((1 - p_drop_a) ** (3 - Y))
    p_Y_b = p_phone_b * choose(3, Y) * (p_drop_b ** Y) * ((1 - p_drop_b) ** (3 - Y))
    return p_Y_a + p_Y_b

def p_XY(X, Y, p_phone_a, p_phone_b, p_drop_a, p_drop_b):
    if X < Y:
        return 0
    p_XY_a = p_phone_a * choose(3, Y) * (p_drop_a ** Y) * ((1 - p_drop_a) ** (3 - Y)) * choose(3, X - Y) * (p_drop_a ** (X - Y)) * ((1 - p_drop_a) ** (3 - (X - Y)))
    p_XY_b = p_phone_b * choose(3, Y) * (p_drop_b ** Y) * ((1 - p_drop_b) ** (3 - Y)) * choose(3, X - Y) * (p_drop_b ** (X - Y)) * ((1 - p_drop_b) ** (3 - (X - Y)))
    return p_XY_a + p_XY_b

def p8():
    p_phone_a = .5
    p_phone_b = 1.0 - p_phone_a
    p_drop_a = .1
    p_drop_b = .25
    P_Yis1 = p_Y(1, p_phone_a, p_phone_b, p_drop_a, p_drop_b)
    print("P_Y(Y = 1) = %.4g" %P_Yis1)
    E_XgivenY = 0.0
    for i in range(1, 5):
        E_XgivenY += i * (p_XY(i, 1, p_phone_a, p_phone_b, p_drop_a, p_drop_b) / P_Yis1)
    print("E[X | Y = 1] = %.4g" %E_XgivenY)

def print_p2():
    p2()

def print_p4():
    p4()

def print_p5():
    p5()

def print_p8():
    p8()

def main():
    #print_p2()
    #print_p4()
    #print_p5()
    print_p8()

if __name__ == '__main__':
    main()

