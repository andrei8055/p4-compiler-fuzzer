from randomizer import randomizer
from tuple_keyset_expression import tuple_keyset_expression
from simple_keyset_expression import simple_keyset_expression
from common import common


class keyset_expression(object):
	type = None
	types = ["tupleKeysetExpression", "simpleKeysetExpression"]
	probabilities = [0, 100]
	value = None

	# keysetExpression
	# : tupleKeysetExpression
	# | simpleKeysetExpression
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		common.usedRandomize()
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.value = tuple_keyset_expression()
		elif self.type == 1:
			self.value = simple_keyset_expression()
		self.value.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.value.generate_code()
