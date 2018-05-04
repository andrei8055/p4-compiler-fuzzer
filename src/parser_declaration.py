from parser_type_declaration import parser_type_declaration
from opt_constructor_parameters import opt_constructor_parameters
from parser_local_elements import parser_local_elements
from parser_states import parser_states
from common import common


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
		common.usedRandomize()
		self.parser_type_declaration = parser_type_declaration()
		self.parser_type_declaration.randomize()
		self.opt_constructor_parameters = opt_constructor_parameters()
		self.opt_constructor_parameters.randomize()
		self.parser_local_elements = parser_local_elements()
		self.parser_local_elements.randomize()
		self.parser_states = parser_states()
		self.parser_states.randomize()

	def generate_code(self):
		code = self.parser_type_declaration.generate_code() + ' '
		code += self.opt_constructor_parameters.generate_code() + ' {'
		code += self.parser_local_elements.generate_code() + ' '
		code += self.parser_states.generate_code() + '} '
		return code
