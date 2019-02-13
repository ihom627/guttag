#!/usr/bin/env python
"""random_walk.py: Random walk with bias"""
__author__ = "Ivan Hom"

DEBUG = 0 
X_DIM = 10000
Y_DIM = 10000

import random
import pandas as pd
import numpy as np


def take_step_no_bias():
	step_choices = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
	return random.choice(step_choices) 


def take_step_ew_bias():
	step_choices = [(0 ,1), (0, -1), (1, 0), (1, 0), (-1, 0), (-1, 0)]
	return random.choice(step_choices)


def take_step_ns_bias():
	step_choices = [(0 ,1), (0, 1), (0, -1), (0, -1), (1, 0), (-1, 0)]
	return random.choice(step_choices)


def do_steps(steps_max, bias = 0):
	#init  
	random.seed(999)
	array = np.zeros([X_DIM, Y_DIM], dtype=int)
	if DEBUG > 1: 
		print("array dim=", array.ndim, " shape =", array.shape, " size=", array.size, " dtype=", array.dtype)
	x_loc_new = x_loc_old = X_DIM /2
	y_loc_new = y_loc_old = Y_DIM /2

	#steps 
	for i in range (0, steps_max):
		if bias ==0:
			step_x, step_y = take_step_no_bias()
		elif bias ==1:
			step_x, step_y = take_step_ew_bias()
		elif bias ==2:
                        step_x, step_y = take_step_ns_bias()
		if DEBUG >1:
			print("this is step_x= ", step_x, " step_y = ", step_y)	
		x_loc_new = int(x_loc_old + step_x) 
		y_loc_new = int(y_loc_old + step_y) 
		if DEBUG >0:
			print("this is x_loc_new=", x_loc_new, "y_loc_new =", y_loc_new)
		array[x_loc_new, y_loc_new] +=1 
		x_loc_old = x_loc_new
		y_loc_old = y_loc_new
	if DEBUG >1:
		for i in range(0, X_DIM):
			for j in range(0, Y_DIM):
				if array[i, j] >0:
					print("array, i=", i, "j=", j, "=", array[i, j])

	dist_x = (X_DIM/2 - x_loc_new)
	dist_y = (X_DIM/2 - y_loc_new)
	overall_dist = (dist_x**2 + dist_y**2)**.5
	print("for steps=", steps_max, "overall_dist=", overall_dist, "x_loc=", x_loc_new, "y_loc=", y_loc_new)


def main():
	#no bias
	print("with no bias")
	do_steps(10, 0)	
	do_steps(100, 0)	
	do_steps(1000, 0)	
	do_steps(10000, 0)	
	do_steps(100000, 0)	

	#ew bias
	print("with ew bias")	
	do_steps(10, 1)
	do_steps(100, 1)
	do_steps(1000, 1)
	do_steps(10000, 1)
	do_steps(100000, 1)

	#ns bias
	print("with ns bias")
	do_steps(10, 2)
	do_steps(100, 2)
	do_steps(1000, 2)
	do_steps(10000, 2)
	do_steps(100000, 2)



if __name__ == "__main__":
        main()









#################  OLD ####################

#class walker(object):
#	def __init__(self, name = "default"):
#		self.name = name
#		
#	def __str__(self):
#		return self.name
#
#
#class loc(object):
#	def __init__(self, x_loc, y_loc):
#		self.x_loc, self.y_loc = x_loc, y_loc
#
#	def move(self, delta_x, delta_y):
#		return(self.x_loc + delta_x, self.y_loc + delta_y)
#
#	def get_x_loc(self):
#		return(self.x_loc)
#
#	def get_y_loc(self):
#		return(self.y_loc)
#
#	def calc_dist(self, other):
#		other_x_loc, other_y_loc = other.x_loc, other.y_loc
#		x_delta, y_delta = self.x_loc - other_x_loc, self.y_loc - other_y_loc		
#		return (x_delta**2 + y_delta**2)**.5
#
#	def __str__(self):
#		return '<' + str(self.x_loc) + ', ' + str(self.y_loc) + '>'
#
#
#class field(object):
#	def __init__(self):
#		self.walkers = {}
#
#	def add_walker(self, walker, loc):
#		self.walkers[walker] = loc
#
#	def move_walker(self, walker):
#		x_dist, y_dist = walker.take_step()
#		current_loc = self.walkers[walker]
#		self.walkers[walker] = current_loc.move(x_dist, y_dist)
#
#	def get_loc(self, walker):
#		return self.walkers[walker]
#


