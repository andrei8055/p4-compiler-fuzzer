from expression import expression
from switch_casses import switch_casses
from common import common


class switch_statement(object):
	type = 'switch_statement'
	expression = None
	switch_casses = None

	# switchStatement
	# : SWITCH '(' expression ')' '{'switchCases '}'
	# ;

	def __init__(self, expression=None, switch_casses=None):
		self.expression = expression
		self.switch_casses = switch_casses

	def randomize(self):
		common.usedRandomize()
		self.expression = expression()
		self.expression.randomize()
		self.switch_casses = switch_casses()
		self.switch_casses.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'switch (' + self.expression.generate_code() + ') {' + self.switch_casses.generate_code() + '} '
