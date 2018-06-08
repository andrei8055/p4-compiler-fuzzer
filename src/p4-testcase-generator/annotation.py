from name import name
from expression_list import expression_list
from randomizer import randomizer
from common import common


class annotation(object):
	type = None
	types = ["name", "nameExpressionList"]
	# TODO: implement nameExpressionList and set probability higher than 0 for it
	probabilities = [100, 0]
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
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.name = name()
			self.name.randomize()
		elif self.type == 1:
			self.name = name()
			self.name.randomize()
			self.expression_list = expression_list()
			self.expression_list.randomize()


	def generate_code(self):
		common.usedCodeGenerator(self)
		code = '@' + self.name.generate_code()
		if self.expression_list is not None:
			code += '(' + self.expression_list.generate_code() + ')'
		return code