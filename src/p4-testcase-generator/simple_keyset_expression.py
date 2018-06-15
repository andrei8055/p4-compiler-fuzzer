from randomizer import randomizer
from expression import expression
from default_literal import default_literal
from dontcare_literal import dontcare_literal
from mask_expression import mask_expression
from range_expression import range_expression
from common import common


class simple_keyset_expression(object):
	type = None
	types = ["expression", "DEFAULT", "DONTCARE", "expressionMASKexpression", "expressionRANGEexpression"]
	probabilities = [0, 50, 50, 0, 0]
	value = None

	# simpleKeysetExpression
	# : expression
	# | DEFAULT
	# | DONTCARE
	# | expression MASK expression
	# | expression RANGE expression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = expression()
		elif self.type == 1:
			self.value = default_literal()
		elif self.type == 2:
			self.value = dontcare_literal()
		elif self.type == 3:
			self.value = mask_expression()
		elif self.type == 4:
			self.value = range_expression()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
