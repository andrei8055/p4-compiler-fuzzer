import argparse
from pyclustering.cluster.kmedoids import kmedoids
import mysql.connector
import math
import p4fuzzclib
import sys
from datetime import datetime
from nltk.metrics import edit_distance

def main():
	argparse.ArgumentParser(description="P4Fuzz Bugs Tamer")

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()

	caseIds = []
	caseErrors = []

	cursor.execute("DELETE FROM tamed_bugs")
	cnx.commit()

	cursor.execute("SELECT id, error FROM bugs WHERE id < 3200")
	for (id, error) in cursor:
		caseIds.append(id)
		caseErrors.append(str(error))

	dt = datetime.now()
	print "Loading data from database..."


	dt2 = datetime.now()
	diff = dt2 - dt
	print str(diff.total_seconds() * 1000) + " Loaded data from database"

	dist_tuple = p4fuzzclib.calc_distance_matrix(caseErrors)
	dist = [list(x) for x in dist_tuple]

	dt3 = datetime.now()
	diff = dt3 - dt2
	print str(diff.total_seconds()) + " Calculated distances using token"

	# dists = [edit_distance(caseErrors[i], caseErrors[j])
	# 		for i in range(1, len(caseErrors))
	# 		for j in range(0, i)]
	#
	# dt7 = datetime.now()
	# diff = dt7 - dt3
	# print str(diff.total_seconds()) + " Calculated distances using lev"

	# sys.exit()

	initial_medoids = [0, len(caseErrors)-1]

	kmedoids_instance = kmedoids(dist, initial_medoids, 10, data_type='distance_matrix')
	kmedoids_instance.process()
	clusters = kmedoids_instance.get_clusters()
	medoids = kmedoids_instance.get_medoids()

	print "Clustered #1 ..."

	has_large = True
	cnt = 1
	while has_large:
		cnt += 1
		has_large = False
		for i, cluster in enumerate(clusters):
			medoid = medoids[i]
			medoid_distances = dist[medoid]
			max_points = p4fuzzclib.calc_max_distance_cluster(dist_tuple, cluster)
			max_dist = dist[max_points[0]][max_points[1]]
			if max_dist > 60:
				has_large = True
				new_medoid = max_points[0] if medoid_distances[max_points[0]] > medoid_distances[max_points[1]] else max_points[1]
				initial_medoids = medoids
				initial_medoids.append(new_medoid)
				kmedoids_instance = kmedoids(dist, initial_medoids, 100, data_type='distance_matrix')
				kmedoids_instance.process()
				clusters = kmedoids_instance.get_clusters()
				medoids = kmedoids_instance.get_medoids()
			else:
				print "Cluster " + str(i) + ": " + str(max_dist)
		print "Clustered #" + str(cnt) + " ..."

	dt4 = datetime.now()
	diff = dt4 - dt3
	print str(diff.total_seconds() * 1000) + " Clustering finished"

	for i, cluster in enumerate(clusters):
		medoid = medoids[i]
		for error_index in cluster:
			is_medoid = True if medoid == error_index else False
			data = (caseIds[error_index], i, is_medoid)
			cursor.execute("INSERT INTO tamed_bugs (`bug_id`, `cluster`, `is_medoid`) VALUES (%s, %s, %s)", data)
			cnx.commit()

	dt5 = datetime.now()
	diff = dt5 - dt4
	print str(diff.total_seconds() * 1000) + " Tamed bugs clusters inserted into database finished! All Done!"

	dt6 = datetime.now()
	diff = dt6 - dt
	print "Total time: " + str(diff.total_seconds())


def andrei_distance(string1, string2):
	string1_tokens = string1.split(' ')
	string2_tokens = string2.split(' ')
	init_dist = dist = len(string1_tokens) + len(string2_tokens)
	for token1 in string1_tokens:
		new_string2_tokens = []
		found = False
		for token2 in string2_tokens:
			if token1 == token2 and not found:
				dist -= 2
				found = True
			else:
				new_string2_tokens.append(token2)
		string2_tokens = new_string2_tokens
	return int(math.floor((dist / (init_dist * 1.0)) * 100))


if __name__ == '__main__':
	main()