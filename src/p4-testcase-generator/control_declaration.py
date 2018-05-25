from control_type_declaration import control_type_declaration
from opt_constructor_parameters import opt_constructor_parameters
from control_local_declarations import control_local_declarations
from control_body import control_body
from common import common


class control_declaration(object):
	type = 'control_declaration'
	control_type_declaration = None
	opt_constructor_parameters = None
	control_local_declarations = None
	control_body = None

	# controlDeclaration
	# : controlTypeDeclaration optConstructorParameters
	# / *no type parameters allowed in controlTypeDeclaration * /
	# '{'controlLocalDeclarations APPLY controlBody '}' \
	# ;

	def __init__(self, control_type_declaration=None, opt_constructor_parameters=None, control_local_declarations=None, control_body=None):
		self.control_type_declaration = control_type_declaration
		self.opt_constructor_parameters = opt_constructor_parameters
		self.control_local_declarations = control_local_declarations
		self.control_body = control_body

	def randomize(self):
		common.usedRandomize()
		self.control_type_declaration = control_type_declaration()
		self.control_type_declaration.randomize()
		self.opt_constructor_parameters = opt_constructor_parameters()
		self.opt_constructor_parameters.randomize()
		self.control_local_declarations = control_local_declarations()
		self.control_local_declarations.randomize()
		self.control_body = control_body()
		self.control_body.randomize()

	def generate_code(self):
		return self.control_type_declaration.generate_code() + ' ' + self.opt_constructor_parameters.generate_code() + '{ ' + self.control_local_declarations.generate_code() + ' apply ' + self.control_body.generate_code() + '}'
