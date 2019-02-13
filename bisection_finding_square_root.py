#!/usr/bin/env python
"""bisection_finding_square_root.py: bisection approach for finding square root of a number within epsilon of 0.1"""
__author__ = "Ivan Hom"


def bisection(number, epsilon = 0.01):
	num_guesses = 0
	low = 0
	high = number 
	ans = (high + low)/2.0
	while abs(ans**2 - number) >= epsilon:
		num_guesses += 1
		if ans**2 < number:
			low = ans
		else:
			high = ans
		ans = (high + low)/2.0
	print('num_guesses =', num_guesses)
	print(ans, 'is close to square root of', number)


def main(): 
        bisection(25) 
        bisection(64) 
        bisection(75) 
        bisection(100) 
 
 
 
if __name__ == "__main__": 
        main() 



