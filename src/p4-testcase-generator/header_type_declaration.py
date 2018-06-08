from opt_annotations import opt_annotations
from name import name
from scope import scope
from common import common


class header_type_declaration(object):
	type = 'header_type_declaration'

	opt_annotations = None
	name = None
	struct_field_list = None

	# headerTypeDeclaration
	# : optAnnotations HEADER name '{' structFieldList '}'
	# ;

	def __init__(self, opt_annotations=None, name=None, struct_field_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.struct_field_list = struct_field_list

	def randomize(self):
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			from struct_field_list import struct_field_list
			self.struct_field_list = struct_field_list(fromObj=self)
			self.struct_field_list.randomize()
			if not self.filter():
				break
		scope.insert_type(self.name.generate_code(), "header")

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + 'header ' + self.name.generate_code() + ' ' + '{' + self.struct_field_list.generate_code() + '}\n\n'

	def filter(self):
		available_types = scope.get_available_types()
		if self.name.generate_code() in available_types:
			return True
		return False
