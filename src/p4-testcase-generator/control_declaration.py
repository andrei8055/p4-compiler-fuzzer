from control_type_declaration import control_type_declaration
from opt_constructor_parameters import opt_constructor_parameters
from control_declaration_creation import control_declaration_creation
from control_body import control_body
from common import common
from scope import scope


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
		scope.start_local()
		if self.control_type_declaration.parameter_list.non_empty_parameter_list is not None:
			for _parameter in self.control_type_declaration.parameter_list.non_empty_parameter_list.parameter_list:
				scope.insert_parameter(_parameter.name.generate_code(), _parameter.type_ref.get_ref_type(), _parameter)
		self.opt_constructor_parameters = opt_constructor_parameters()
		self.opt_constructor_parameters.randomize()
		scope.start_local()
		self.control_local_declarations = control_declaration_creation()
		self.control_local_declarations.randomize()
		scope.stop_local()
		self.control_body = control_body()
		self.control_body.randomize()
		scope.stop_local()

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.control_type_declaration.generate_code() + ' ' + self.opt_constructor_parameters.generate_code() + '{ ' + self.control_local_declarations.generate_code() + ' apply ' + self.control_body.generate_code() + '}'
