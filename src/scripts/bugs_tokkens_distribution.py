import mysql.connector

def main():

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()
	cursor2 = cnx.cursor()

	tokens = []
	sizes = []

	cursor.execute("SELECT sq.* FROM (SELECT t.tokens, t.f_size FROM tests t INNER JOIN bugs b ON b.test = t.test WHERE t.`compile_time` IS NOT NULL) sq ORDER BY tokens ASC")

	avgs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

	for (token, size) in cursor:
		index = token / 1000
		if index <= 17:
			avgs[index][0] += 1

	cursor2.execute("SELECT sq.* FROM (SELECT t.tokens, t.f_size FROM tests t WHERE `compile_time` IS NOT NULL) sq ORDER BY tokens ASC")

	avgs2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
	for (token, size) in cursor2:
		index = token / 1000
		if index <= 17:
			avgs2[index][0] += 1

	str_builder1 = ""
	str_builder2 = ""
	for i, avg in enumerate(avgs):
		i1 = avg[0]
		i2 = avgs2[i][0]
		str_builder1 += str(i1) + ","
		str_builder2 += str(i2) + ","
	str_builder1 = str_builder1[:-1]
	str_builder2 = str_builder2[:-1]
	print str_builder1
	print str_builder2

if __name__ == '__main__':
	main()