#!/usr/bin/env python
"""quicksort.py: perform quicksort on a list of integers"""
__author__ = "Ivan Hom"

DEBUG = 0 


def quicksort(intermediate_list):
	left_list = []
	right_list = []
	left_result = []	
	right_result = []	
	result_list = []	

	list_index = 0
	pivot = 0

	if DEBUG ==1:
		print("quicksort() with intermediate_list=", intermediate_list)

	if len(intermediate_list) < 2:
		return(intermediate_list)
	else:
		pivot = intermediate_list[0]

		for list_index in range (1, len(intermediate_list)):
			if (intermediate_list[list_index]) <= pivot:
				left_list.append(intermediate_list[list_index])
			else:
				right_list.append(intermediate_list[list_index])					

	#append the pivot at the end of the left_list
	left_list.append(pivot)

	if DEBUG ==1:
		print("quicksort() with left_list=", left_list)
		print("quicksort() with right_list=", right_list)
	left_result = quicksort(left_list)	
	right_result = quicksort(right_list)	
	return(left_result + right_result)


def main():
	#debugging
	#import pdb; pdb.set_trace()

	input_list = [1, 4, 3, 7, 5]
	print("this is the input_list=", input_list)
	final_list = quicksort(input_list)
	print("this is final_list=", final_list)


	input_list = [9, 8, 7, 6, 1, 4, 3, 2, 5]
	print("this is the input_list=", input_list)
	final_list = quicksort(input_list)
	print("this is final_list=", final_list)


if __name__ == "__main__":
        main()


	













