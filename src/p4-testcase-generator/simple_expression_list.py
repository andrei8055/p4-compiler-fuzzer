from simple_keyset_expression import simple_keyset_expression
from randomizer import randomizer


class simple_expression_list(object):
	type = 'simple_expression_list'
	expression_list = []
	min_list_size = 1
	max_list_size = 5

	def __init__(self, expression_list=None):
		self.expression_list = expression_list if expression_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_simple_keyset_expression = simple_keyset_expression()
			_simple_keyset_expression.randomize()
			self.expression_list.append(_simple_keyset_expression)

	def generate_code(self):
		code = ''
		for x in range(0, len(self.expression_list)):
			code += self.expression_list[x].generate_code()
			if x < len(self.expression_list) - 1:
				code = code + ', '
		return code
