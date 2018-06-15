from keyset_expression import keyset_expression
from common import common
from scope import scope
from randomizer import randomizer


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
		available_states = scope.get_available_states()
		self.name = available_states.keys()[randomizer.randint(0, len(available_states) - 1)]

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.keyset_expression.generate_code() + ' : ' + self.name + ' ; '
