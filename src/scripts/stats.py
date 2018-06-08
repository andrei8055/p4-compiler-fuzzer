import mysql.connector

def main():

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()

	tokens = []
	sizes = []

	cursor.execute("SELECT sq.* FROM (SELECT tokens, generate_time FROM tests WHERE generate_time IS NOT NULL AND compile_time IS NOT NULL) sq ORDER BY tokens ASC")

	avgs = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

	for (token, size) in cursor:
		index = token / 1000
		if index <= 17:
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

	# str_tokens = ""
	# for token in tokens:
	# 	str_tokens += str(token) + ","
	# str_tokens = str_tokens[:-1]
	# print "Tokens: [" +  str_tokens + "]"
	#
	# str_sizes = ""
	# for size in sizes:
	# 	str_sizes += str(size) + ","
	# str_sizes = str_sizes[:-1]
	# print "Times: [" + str_sizes + "]"

if __name__ == '__main__':
	main()