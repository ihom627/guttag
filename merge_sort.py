#!/usr/bin/env python
"""merge_sort.py: perform merge sort on a list of integers"""
__author__ = "Ivan Hom"

DEBUG = 0 

def merge(left_list, right_list):
	if DEBUG == 1:
		print("inside merge_sort() left_list=", left_list, "right_list=", right_list)
	merged_list = []

	left_index = 0
	right_index = 0
  
	#do comparison
	while left_index < len(left_list) and right_index < len(right_list):
		if left_list[left_index] < right_list[right_index]:
			merged_list.append(left_list[left_index])
			left_index += 1
		else:
			merged_list.append(right_list[right_index])
			right_index += 1
	
	#copy over the rest of the list if the other side is empty
	while (left_index < len(left_list)):
		merged_list.append(left_list[left_index])
		left_index += 1
	while (right_index < len(right_list)):
		merged_list.append(right_list[right_index])
		right_index += 1
	
	return merged_list


def merge_sort(intermediate_list):
	if len(intermediate_list) < 2:
		return(intermediate_list)
	else:
		middle = int(len(intermediate_list)/2)
		left = merge_sort(intermediate_list[:middle])				
		right = merge_sort(intermediate_list[middle:])				
		return merge(left, right)


def main():
	input_list = [1, 4, 3, 7, 5]
	print("this is the input_list=", input_list)
	final_list = merge_sort(input_list)
	print("this is final_list=", final_list)


	input_list = [9, 8, 7, 6, 1, 4, 3, 2, 5]
	print("this is the input_list=", input_list)
	final_list = merge_sort(input_list)
	print("this is final_list=", final_list)


if __name__ == "__main__":
        main()


	













