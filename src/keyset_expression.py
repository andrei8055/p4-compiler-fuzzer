import random
from tuple_keyset_expression import tuple_keyset_expression
from simple_keyset_expression import simple_keyset_expression
from common import common


class keyset_expression(object):
	type = 'keyset_expression'
	value = None

	# keysetExpression
	# : tupleKeysetExpression
	# | simpleKeysetExpression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.value = tuple_keyset_expression()
		elif rnd == 1:
			self.value = simple_keyset_expression()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
