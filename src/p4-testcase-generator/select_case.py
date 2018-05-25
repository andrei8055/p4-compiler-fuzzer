from keyset_expression import keyset_expression
from name import name
from common import common


class select_case(object):
	type = 'select_case'
	keyset_expression = None
	name = None

	# selectCase
	# : keysetExpression ':' name ';'
	# ;

	def __init__(self, keyset_expression=None, name=None):
		self.keyset_expression = keyset_expression
		self.name = name

	def randomize(self):
		common.usedRandomize()
		self.keyset_expression = keyset_expression()
		self.keyset_expression.randomize()
		self.name = name()
		self.name.randomize()

	def generate_code(self):
		return self.keyset_expression.generate_code() + ' : ' + self.name.generate_code() + ' ; '