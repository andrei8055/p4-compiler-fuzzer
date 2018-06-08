import mysql.connector

def main():

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()

	tokens = []
	sizes = []

	cursor.execute("SELECT sq.* FROM (SELECT tokens, compile_time FROM tests WHERE compile_time IS NOT NULL) sq ORDER BY tokens ASC")

	items = 0
	sum = 0.0
	avgs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

	for (token, size) in cursor:
		index = token / 1000
		if index <= 17:
			items += 1
			sum += size
			avgs[index][0] += 1
			avgs[index][1] += size
			tokens.append(token)
			sizes.append(size)

	str_builder = ""
	for avg in avgs:
		i = avg[0] if avg[0] > 0 else 1
		size = avg[1]
		str_builder += str(round(size / i, 3)) + ","
	str_builder = str_builder[:-1]
	print "(" + str_builder + ")"

	print "Avg per case: " + str(sum / items)

if __name__ == '__main__':
	main()