from common import common
import random


class annotation(object):
	name = ''
	expression_list = []
	name_min_length = 1
	name_max_length = 50

	def __init__(self, name='', expression_list=[]):
		self.name = name
		self.expression_list = expression_list

	def get_name(self):
		return self.name

	def get_expression_list(self):
		return self.expression_list

	def randomize(self):
		self.name = common.get_random_string(random.randint(self.name_min_length, self.name_max_length), False)
		self.expression_list = [] #todo generate random expression list

	def generate_code(self):
		code = ''
		if len(self.get_expression_list()) > 0:
			code += '@'
			code += self.get_name()
			code += '('
			expression_list = self.get_expression_list()
			for x in range(0, len(expression_list)):
				code = code + '"' + str(expression_list[x]) + '"'
				if x < len(expression_list) - 1:
					code = code + ', '
			code += ')'
		return code