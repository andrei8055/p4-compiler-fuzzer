from scope import scope
from common import common
from type_ref import type_ref
from randomizer import randomizer


class assignment_statement(object):
	type = 'assignment_declaration'
	type_ref = None
	lvalue = None
	expression = None

	# | lvalue '=' expression ';'

	def __init__(self, lvalue=None, expression=None):
		self.lvalue = lvalue
		self.expression = expression

	def randomize(self):
		common.usedRandomize()
		while True:
			self.type_ref = type_ref(force_type=0)
			self.type_ref.randomize()
			available_variables = scope.get_available_variables(only_types=self.type_ref.get_ref_type())
			if len(available_variables):
				self.lvalue = available_variables.keys()[randomizer.randint(0, len(available_variables) - 1)]
				self.expression = self.type_ref.value.generate_literal()
				if not self.filter():
					break

	def filter(self):
		if self.type_ref.get_ref_type() in ["varbit", "error"]:
			return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.lvalue + ' = ' + self.expression + ';'

