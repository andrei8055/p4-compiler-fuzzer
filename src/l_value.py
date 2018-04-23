from l_values.l_value_dot_member import l_value_dot_member
from prefixed_non_type import prefixed_non_type
from l_values.l_value_expression import l_value_expression
from l_values.l_value_expression_expression import l_value_expression_expression

import random


class l_value:
	type = 'l_value'
	lvalue = None

	# lvalue
	# 	: prefixedNonTypeName
	# 	| lvalue '.' member
	# 	| lvalue '[' expression ']'
	# 	| lvalue'['expression':'expression']'

	def randomize(self):
		rnd = random.randint(0, 3)
		if rnd == 0:
			self.lvalue = prefixed_non_type()
		elif rnd == 1:

		self.lvalue.randomize()

