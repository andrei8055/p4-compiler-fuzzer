import argparse
from pyclustering.cluster.kmedoids import kmedoids
import mysql.connector
import math
import p4fuzzclib
import sys
from datetime import datetime

def main():
	argparse.ArgumentParser(description="P4Fuzz Bugs Tamer")

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()

	caseIds = []
	caseErrors = []

	cursor.execute("DELETE FROM tamed_bugs")
	cnx.commit()

	cursor.execute("SELECT id, error FROM bugs")
	for (id, error) in cursor:
		caseIds.append(id)
		caseErrors.append(str(error))

	dt = datetime.now()
	print "Loading data from database..."


	dt2 = datetime.now()
	diff = dt2 - dt
	print str(diff.total_seconds() * 1000) + " Loaded data from database"

	dist = p4fuzzclib.calc_distance_matrix(caseErrors)
	dist = [list(x) for x in dist]

	dt3 = datetime.now()
	diff = dt3 - dt2
	print str(diff.total_seconds() * 1000) + " Calculated distances"

	initial_medoids = [0, len(caseErrors)-1]

	kmedoids_instance = kmedoids(dist, initial_medoids, 10, data_type='distance_matrix')
	kmedoids_instance.process()
	clusters = kmedoids_instance.get_clusters()
	medoids = kmedoids_instance.get_medoids()

	print "Clustered #1 ..."

	done = False
	cnt = 1
	while not done:
		cnt += 1
		for i, cluster in enumerate(clusters):
			max_dist = 0
			new_medoid = None
			medoid = medoids[i]
			medoid_distances = dist[medoid]
			for error_index in cluster:
				if medoid_distances[error_index] > max_dist:
					max_dist = medoid_distances[error_index]
					new_medoid = error_index
			if max_dist > 40:
				initial_medoids = medoids
				initial_medoids.append(new_medoid)
				kmedoids_instance = kmedoids(dist, initial_medoids, 100, data_type='distance_matrix')
				kmedoids_instance.process()
				clusters = kmedoids_instance.get_clusters()
				medoids = kmedoids_instance.get_medoids()
			else:
				done = True
		print "Clustered #" + str(cnt) + " ..."

	for i, cluster in enumerate(clusters):
		medoid = medoids[i]
		for error_index in cluster:
			is_medoid = True if medoid == error_index else False
			data = (caseIds[error_index], i, is_medoid)
			cursor.execute("INSERT INTO tamed_bugs (`bug_id`, `cluster`, `is_medoid`) VALUES (%s, %s, %s)", data)
			cnx.commit()


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