from opt_annotations import opt_annotations
from parameter_list import parameter_list
from opt_type_parameters import opt_type_parameters
from name import name
from common import common


class parser_type_declaration(object):
	opt_annotations = None
	name = None
	opt_type_parameters = None
	parameter_list = None
	type = 'parser_type_declaration'

	# parserTypeDeclaration
	# : optAnnotations PARSER name optTypeParameters '(' parameterList')' ;

	def __init__(self, opt_annotations=None, name=None, opt_type_parameters=None, parameter_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.opt_type_parameters = opt_type_parameters
		self.parameter_list = parameter_list

	def get_name(self):
		return self.name

	def randomize(self):
		common.usedRandomize()
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			self.opt_type_parameters = opt_type_parameters()
			self.opt_type_parameters.randomize()
			self.parameter_list = parameter_list()
			self.parameter_list.randomize()
			if not self.filter():
				break

	def filter(self):
		if self.parameter_list.non_empty_parameter_list is None:
			return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + 'parser ' + self.name.generate_code() + self.opt_type_parameters.generate_code() + '(' + self.parameter_list.generate_code() + ')'
