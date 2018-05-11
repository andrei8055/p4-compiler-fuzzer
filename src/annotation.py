from common import common
from name import name
from expression_list import expression_list
import random


class annotation(object):
	name = None
	expression_list = None
	name_min_length = 1
	name_max_length = 50

	# annotation
	# : '@' name
	# | '@' name '(' expressionList ')'
	# ;

	def __init__(self, name=None, expression_list=None):
		self.name = name
		self.expression_list = expression_list

	def get_name(self):
		return self.name

	def get_expression_list(self):
		return self.expression_list

	def randomize(self):
		common.usedRandomize()
		self.name = name()
		self.name.randomize()
		rnd = random.randint(0,1)
		if rnd == 0:
			self.expression_list = expression_list()
			self.expression_list.randomize()


	def generate_code(self):
		code = '@' + self.name.generate_code()
		if self.expression_list is not None:
			code += ' ' + self.expression_list.generate_code()
		return code