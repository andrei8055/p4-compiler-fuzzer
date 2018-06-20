from expression_list import expression_list
from select_case_list import select_case_list
from common import common
from scope import scope
from randomizer import randomizer


class select_expression(object):
	type = 'select_expression'
	expression_list = None
	select_case_list = None
	parameter = None
	member = None

	# selectExpression
	# : SELECT '(' expressionList ')' '{'selectCaseList '}'
	# ;

	def __init__(self, expression_list=None, select_case_list=None):
		self.expression_list = expression_list
		self.select_case_list = select_case_list

	def randomize(self):
		common.usedRandomize()
		available_parameters = scope.get_available_parameters(["struct", "header"])
		if len(available_parameters):
			self.parameter = available_parameters.keys()[randomizer.randint(0, len(available_parameters) - 1)]
			_parameter = available_parameters[self.parameter]["object"].type_ref.get_type_decl()
			if len(_parameter.struct_field_list.field_list):
				_field_list = []
				for _field in _parameter.struct_field_list.field_list:
					if _field.type_ref.type == 0 and _field.type_ref.get_ref_type() != "varbit":
						_field_list.append(_field)
				if len(_field_list):
					self.member = _field_list[randomizer.randint(0, len(_field_list) - 1)]
					self.select_case_list = select_case_list()
					self.select_case_list.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return 'select(' + self.parameter + '.' + self.member.name.generate_code() + '){\n' + self.select_case_list.generate_code() + '\n}'
