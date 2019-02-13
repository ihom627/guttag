#!/usr/bin/env python
"""kmeans_clustering.py: performing kmeans clustering"""
__author__ = "Ivan Hom"

DEBUG = 0

import random

MAX_ITERATIONS = 3

# class of for each instance
class example(object):

	def __init__(self, name, features, centroid_name = None):
		#feature is an array of floats
		self.name = name
		self.features = features
		self.centroid_name = centroid_name 

	def get_dimensionality(self):
		return(len(self.features))

	def get_features(self):
		return(self.features[:])

	def get_centroid_name(self):
		return(self.centroid_name)

	def set_centroid_name(self, centroid_name):
		self.centroid_name = centroid_name

	def get_name(self):
		return(self.name)

	def calc_minkowski_distance(self, other, p = 2):
		#assume feature vectors have the same length
		dist = 0
		for i in range(0, len(self.features)):
			dist += abs(self.features[i] - other.features[i])**p
		print("dist =", dist)
		return(dist**(1/2))

	def calc_minkowski_distance_from_centroid(self, centroid_features, p = 2):
		#pass in centroid location
		dist = 0
		for i in range(0, len(self.features)):
			dist += abs(self.features[i] - centroid_features[i])**p
		return(dist**(1/2))

	def __str__(self):
		return(self.name +':'+str(self.features) + ':' + str(self.centroid_name))		


class cluster(object):

	def __init__(self, name, features):
		self.name = name
		self.centroid_features = features 

	def get_name(self):
		return(self.name)

	def compute_centroid(self):
		vals = pylab.array([0.0]*self.examples[0].dimensionality())
		for e in self.examples:
			vals += e.get_features()
		centroid = Example('centroid', vals/len(self.examples))
		return(centroid)

	def get_centroid_features(self):
		return(self.centroid_features)

	def set_centroid_feature(self, index, new_value):
		self.centroid_features[index] = new_value

	def variability(self):
		total_dist = 0
		for e in self.example:
			total_dist += (e.minkowski_distance(self.centroid))**2
		return(total_dist)

	def __str__(self):
		return(self.name +':'+str(self.centroid_features))	


#calc centroid	
def calc_centroid(all_examples, all_centroids, feature_vector_length = 0):
	#iterate through centroids
	for centroid_iter in all_centroids:
		centroid_name = centroid_iter.get_name()
		centroid_feature_vector = [0.0] * feature_vector_length
		example_counter = 0
		#iterate through examples
		for example_iter in all_examples:
			example_iter_name = example_iter.get_name()
			in_centroid = example_iter.get_centroid_name()
			#match
			if centroid_name == in_centroid:
				print("found ", example_iter_name, "in centroid ", centroid_name)
				example_counter += 1
				#iterate through features
				ex_features = example_iter.get_features()
				for i in range(0, example_iter.get_dimensionality()):
					if DEBUG >1:
						print("this is feature vector length", example_iter.get_dimensionality())
						print("this is value of i", i)
						print("this is length of the centroid_feature_vector", len(centroid_feature_vector))
					centroid_feature_vector[i] += ex_features[i]
					centroid_iter.set_centroid_feature(i, centroid_feature_vector[i])	
		centroid_feature_vector_temp = centroid_iter.get_centroid_features() 
		for i in range(0, len(centroid_feature_vector)):
			centroid_iter.set_centroid_feature(i, centroid_feature_vector_temp[i]/example_counter)
		if DEBUG >1:
			print("this is centroid_feature_vector =", centroid_feature_vector)


def load_examples(all_examples):
	#example data
	ex0 = example("ex0", [0.5, 0.7, 0.99], "cl0")
	all_examples.append(ex0)
	ex1 = example("ex1", [0.1, 0.5, 0.7], "cl1")
	all_examples.append(ex1)
	ex2 = example("ex2", [0.2, 0.4, 0.6], "cl2")
	all_examples.append(ex2)
	ex3 = example("ex3", [0.3, 0.3, 0.5], "cl3")
	all_examples.append(ex3)
	ex4 = example("ex4", [0.4, 0.2, 0.4], "cl0")
	all_examples.append(ex4)
	ex5 = example("ex5", [0.5, 0.1, 0.3], "cl1")
	all_examples.append(ex5)
	ex6 = example("ex6", [0.6, 0.9, 0.2], "cl2")
	all_examples.append(ex6)
	ex7 = example("ex7", [0.7, 0.8, 0.1], "cl3")
	all_examples.append(ex7)
	ex8 = example("ex8", [0.8, 0.7, 0.99], "cl0")
	all_examples.append(ex8)
	ex9 = example("ex9", [0.9, 0.6, 0.8], "cl0")
	all_examples.append(ex9)
	if DEBUG>1:
		print_examples(all_examples)		


def load_clusters(all_clusters):
	#example clusters
	cl0 = cluster("cl0", [0, 0, 0])
	all_clusters.append(cl0)
	cl1 = cluster("cl1", [1, 0, 0])
	all_clusters.append(cl1)
	cl2 = cluster("cl2", [0, 1, 0])
	all_clusters.append(cl2)
	cl3 = cluster("cl3", [0, 0, 1])
	all_clusters.append(cl3)
	#init random centroid locs
	assign_clusters_initial_centroid_locs(all_clusters)
	if DEBUG>1:
		print_clusters(all_clusters)


def print_examples(all_examples):
	print("all_examples=")
	for i in all_examples:
		i_name = i.get_name()
		i_features = i.get_features()
		i_centroid = i.get_centroid_name()
		print(i_name, i_features, i_centroid)


def print_clusters(all_clusters):
	print("all_clusters=")
	for i in all_clusters:
		i_name = i.get_name()
		i_features = i.get_centroid_features()
		print(i_name, i_features)


def assign_clusters_initial_centroid_locs(all_clusters):
	#perform random assignment at the extreme points
	loc_choices = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	for cluster_iter in all_clusters:
		centroid_feature_vector = cluster_iter.get_centroid_features()
		for i in range(0, len(centroid_feature_vector)):
			if DEBUG > 1:
				print("random assignment of cluster centroid", random.choice(loc_choices))
			cluster_iter.set_centroid_feature(i, random.choice(loc_choices))
		if DEBUG >1:
			print("this is centroid_feature_vector =", cluster_iter.get_centroid_features())


#def tests():
#	#unit test examples
#	name = ex0.get_name()
#	features = ex0.get_features()
#	dimensionality = ex0.get_dimensionality()
#	print("this is example name = ", name, "features =", features, "dimensionality =", dimensionality)
#	name2 = ex1.get_name()
#	features2 = ex1.get_features()
#	dimensionality2 = ex1.get_dimensionality()
#	print("this is example name = ", name2, "features =", features2, "dimensionality =", dimensionality2)
#
#	dist = ex0.calc_minkowski_distance(ex1)
#	print("this is the dist between ex0 and ex1", dist)
#	 
#
#	#unit test clusters
#	name = cl0.get_name()
#	c10_centroid_features = cl0.get_centroid_features()
#	print("this is centroid name =", name, "features =", c10_centroid_features)
#	name = ex0.get_centroid_name()
#	print("ex0 is in centroid =", name)


def	assign_example_to_cluster_centroid(all_examples, all_clusters):
	total_examples_reassigned_counter = 0
	for ex_iter in all_examples:
		closest_dist = 999 
		closest_cluster = "null"
		example_reassigned = 0
		for cluster_iter in all_clusters:
			centroid_features = cluster_iter.get_centroid_features()
			current_dist = ex_iter.calc_minkowski_distance_from_centroid(centroid_features)
			print("example=", ex_iter, "cluster=", cluster_iter, "dist=", current_dist)
			if (current_dist < closest_dist):
				example_reassigned = 1
				closest_dist = current_dist
				closest_cluster = cluster_iter.get_name()
		if ((example_reassigned == 1) and (ex_iter.get_centroid_name() != closest_cluster)): #skip if already in cluster
			if DEBUG ==1:
				print("in assign_example_to_cluster_centroid(): ex_iter=", ex_iter, "reassigned to cluster=", closest_cluster)
			ex_iter.set_centroid_name(closest_cluster)
			total_examples_reassigned_counter += 1
	print("in assign_example_to_cluster_centroid(), examples_reassigned= ", total_examples_reassigned_counter)
	#return the number of examples reassigned to different clusters
	return(total_examples_reassigned_counter)
	
		


def main():
#kmeans clustering


#STEP1: load examples and clusters
	print("STEP1: Load examples and assign random cluster centroid locations")
	#load examples
	all_examples = [] 
	load_examples(all_examples)
	if DEBUG ==1:
		print_examples(all_examples)


	#init clusters 
	all_clusters = []
	load_clusters(all_clusters)
	if DEBUG ==1:
		print_clusters(all_clusters)


#STEP2: calc initial cluster centroid locs
	print("STEP2: Calc initial centroid locs")
	#calc the initial centroid locs
	calc_centroid(all_examples, all_clusters, 3)
	if DEBUG ==1:
		print_clusters(all_clusters)

	#STEP3: while examples moved to new clusters
	examples_moved_to_new_clusters = 10
	iterations = 0
	while ((examples_moved_to_new_clusters > 1) or (iterations > MAX_ITERATIONS)):

	#STEP3: assign each example to nearest centroid
		print("STEP3: Assign examples to nearest centoid")
		examples_moved_to_new_clusters = assign_example_to_cluster_centroid(all_examples, all_clusters)	

	#STEP4: update cluster centoid locs
		print("STEP4: Update centroid locatios")
		calc_centroid(all_examples, all_clusters, 3)
		if DEBUG ==1:
			print_clusters(all_clusters)

		iterations += 1



if __name__ == "__main__":
        main()

