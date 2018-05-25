from randomizer import randomizer
from expression import expression
from default_literal import default_literal
from dontcare_literal import dontcare_literal
from mask_expression import mask_expression
from range_expression import range_expression
from common import common


class simple_keyset_expression(object):
	type = 'simple_keyset_expression'
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
		rnd = randomizer.randint(0, 4)
		if rnd == 0:
			self.value = expression()
		elif rnd == 1:
			self.value = default_literal()
		elif rnd == 2:
			self.value = dontcare_literal()
		elif rnd == 3:
			self.value = mask_expression()
		elif rnd == 4:
			self.value = range_expression()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
