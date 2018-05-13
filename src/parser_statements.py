from parser_statement import parser_statement
import random
from common import common


class parser_statements(object):
	type = 'parser_statements'
	parser_statements_list = []
	min_list_size = 1
	max_list_size = 5

	# parserStatements
	# : / *empty * /
	# | parserStatements parserStatement
	# ;

	def __init__(self, parser_statements_list=None):
		self.parser_statements_list = parser_statements_list if parser_statements_list is not None else []

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.parser_statements_list = []
		else:
			rndl = random.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_parser_statement = parser_statement()
				_parser_statement.randomize()
				self.parser_statements_list.append(_parser_statement)

	def generate_code(self):
		code = ''
		for parser_statement in self.parser_statements_list:
			code += parser_statement.generate_code + ' '
		return code

