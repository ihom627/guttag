#!/usr/bin/env python
"""newton_raphson.py: Newton-Raphson for finding the square root of a number within epsilon of 0"""
__author__ = "Ivan Hom"


# slope = rise/run = f(x1)/delta_x
# by rearranging, delta_x = f(x1)/slope = f(x1)/f'(x1)
# but delta_x = x1 - x2, where x1 > x2
# x2 = x1 - delta_x
# x2 = x1 - f(x1)/f'(x1)


#guess = guess - f(guess)/f'(guess)
#polynomial f is x**2 - k 
#since f is assumed to be a 2nd degree polynomial x**2 - k, f' = 2x

def newton_raphson(number, epsilon = 0.01):
	#epsilon = 0.01
	guess = number/2
	while abs(guess * guess - number) >= epsilon:
		guess = guess - (((guess**2) - number)/(2 * guess))
	print('square root of', number, 'is about', guess)



def main():
	newton_raphson(25)
	newton_raphson(64)
	newton_raphson(75)
	newton_raphson(100)



if __name__ == "__main__":
        main()



