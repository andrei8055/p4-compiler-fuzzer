from opt_annotations import opt_annotations
from non_type_name import non_type_name
from opt_type_parameters import opt_type_parameters
from method_prototypes import method_prototypes


class extern_declaration_method(object):
	type = 'extern_declaration_method'

	opt_annotations = None
	non_type_name = None
	opt_type_parameters = None
	method_prototypes = None

	# : optAnnotations EXTERN nonTypeName optTypeParameters '{' methodPrototypes '}'

	def __init__(self, opt_annotations=None, non_type_name=None, opt_type_parameters=None, method_prototypes=None):
		self.opt_annotations = opt_annotations
		self.non_type_name = non_type_name
		self.opt_type_parameters = opt_type_parameters
		self.method_prototypes = method_prototypes

	def randomize(self):
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.non_type_name = non_type_name()
		self.non_type_name.randomize()
		self.opt_type_parameters = opt_type_parameters()
		self.opt_type_parameters.randomize()
		self.method_prototypes = method_prototypes()
		self.method_prototypes.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' extern ' + self.non_type_name.generate_code() + ' ' + self.opt_type_parameters.generate_code() + '{' + self.method_prototypes.generate_code() + '}'
