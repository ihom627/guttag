#!/usr/bin/env python
"""buffon_laplace_pi_approx.py: Buffon-Laplace methof for approximating pi"""
__author__ = "Ivan Hom"

# inside_circle / iterations = area_circle / area_square
# assume circle is 2 X 2, radius = 1, so area_circle = pi * 1**2 = pi

DEBUG = 1

import random

def get_random_point():
	x_coor = random.random()
	y_coor = random.random()
	return(x_coor, y_coor)


def trial(iterations):
	random.seed(999)
	inside_circle = 0
	outside_circle = 0
	for i in range (0, iterations):
		x_loc, y_loc = get_random_point()
		#inside circle if distance from (0, 0) is less than 1
		dist = (x_loc**2 + y_loc**2)**.5
		if dist < 1:
			inside_circle += 1
			if DEBUG > 1:
				print("inside_circle random point=", x_loc, ", ", y_loc, "dist=", dist)
		else:
			outside_circle += 1	
			if DEBUG >1 :
				print("outside_circle random point=", x_loc, ", ", y_loc, "dist=", dist)

	#only simulated one quadrant, so need to multiply by 4
	pi = 4 * inside_circle / iterations	
	print("STATS: iterations = ", iterations, "pi =", pi, "inside_circle =", inside_circle, "outside_circle=", outside_circle) 	


def main():
	trial(10)	
	trial(100)	
	trial(1000)	
	trial(10000)	
	trial(100000)	
	trial(1000000)	
	#trial(10000000)	
	#trial(100000000)	
	#trial(1000000000)	
	 		

if __name__ == "__main__":
        main()


