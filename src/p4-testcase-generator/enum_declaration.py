from opt_annotations import opt_annotations
from name import name
from identifier_list import identifier_list
from scope import scope
from common import common


class enum_declaration(object):
	type = 'enum_declaration'

	opt_annotations = None
	name = None
	identifier_list = None

	# enumDeclaration
	# : optAnnotations ENUM name '{' identifierList '}'
	# ;

	def __init__(self, opt_annotations=None, name=None, identifier_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.identifier_list = identifier_list

	def randomize(self):
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			self.identifier_list = identifier_list()
			self.identifier_list.randomize()
			if not self.filter():
				break
		scope.insert_type(self.name.generate_code(), "enum", self)

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + ' enum ' + self.name.generate_code() + ' ' + '{' + self.identifier_list.generate_code() + '}'

	def filter(self):
		available_types = scope.get_available_types()
		if self.name.generate_code() in available_types:
			return True
		return False



