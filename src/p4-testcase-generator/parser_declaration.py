from parser_type_declaration import parser_type_declaration
from opt_constructor_parameters import opt_constructor_parameters
from parser_local_elements import parser_local_elements
from parser_states import parser_states
from common import common
from scope import scope


class parser_declaration(object):
	parser_type_declaration = None
	opt_constructor_parameters = None
	parser_local_elements = None
	parser_states = None
	type = 'parser_declaration'

	# parserDeclaration
	# 	: parserTypeDeclaration optConstructorParameters
	# 	/ *no type parameters allowed in the parserTypeDeclaration * /
	# 	'{' parserLocalElements parserStates '}'
	# 	;

	def __init__(self, parser_type_declaration=None, opt_constructor_parameters=None, parser_local_elements=None, parser_states=None):
		self.parser_type_declaration = parser_type_declaration
		self.opt_constructor_parameters = opt_constructor_parameters
		self.parser_local_elements = parser_local_elements
		self.parser_states = parser_states

	def randomize(self):
		self.parser_type_declaration = parser_type_declaration()
		self.parser_type_declaration.randomize()
		self.opt_constructor_parameters = opt_constructor_parameters()
		self.opt_constructor_parameters.randomize()
		scope.start_local()
		if self.parser_type_declaration.parameter_list.non_empty_parameter_list is not None:
			for _parameter in self.parser_type_declaration.parameter_list.non_empty_parameter_list.parameter_list:
				scope.insert_parameter(_parameter.name.generate_code(), _parameter.type_ref.get_ref_type(), _parameter)
		self.parser_local_elements = parser_local_elements()
		self.parser_local_elements.randomize()
		self.parser_states = parser_states()
		self.parser_states.randomize()
		scope.stop_local()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = self.parser_type_declaration.generate_code()
		code += self.opt_constructor_parameters.generate_code() + '{\n'
		code += self.parser_local_elements.generate_code() + '\n'
		code += self.parser_states.generate_code() + '\n}\n\n'
		return code
