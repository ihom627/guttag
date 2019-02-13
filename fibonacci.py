#!/usr/bin/env python
"""fib.py: calculate the fibonacci sequence using recursion and dynamic programming"""
__author__ = "Ivan Hom"

DEBUG = 0
fibonacci_saved_results = {0:1, 1:1}

def fibonacci(number):
	global fibonacci_saved_results
	if DEBUG == 1:
		print("fibonacci called with number", number)
	intermediate_result = 0
	number_minus_1 = 0;
	number_minus_2 = 0;
	if (number == 1) or (number == 0):
		if DEBUG == 1:
			print("returning 1")
		return fibonacci_saved_result[number]
	else:
		if (number -1) in fibonacci_saved_results:
			number_minus_1 = fibonacci_saved_results[number -1]	
		else:
			number_minus_1 = fibonacci(number -1)
			fibonacci_saved_results[number -1] = number_minus_1
		if (number -2) in fibonacci_saved_results:  
                        number_minus_2 = fibonacci_saved_results[number -2]
		else:
			number_minus_2 = fibonacci(number -2)
			fibonacci_saved_results[number -2] = number_minus_2
		intermediate_result = number_minus_1 + number_minus_2 
		if DEBUG == 1:
			print("this is intermediate_result", intermediate_result)
		return (intermediate_result) 
			

def main():
	final_result = fibonacci(8)
	print("fibonacci(8) =", final_result)

	final_result = fibonacci(64)
	print("fibonacci(64) =", final_result)

	final_result = fibonacci(75)
	print("fibonacci(75) =", final_result)

	final_result = fibonacci(100)
	print("fibonacci(100) =", final_result)



if __name__ == "__main__":
        main()


