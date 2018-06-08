from opt_annotations import opt_annotations
from name import name
from struct_field_list import struct_field_list
from common import common
from scope import scope


class struct_type_declaration(object):

	opt_annotations = None
	name = None
	struct_field_list = None

	# structTypeDeclaration
	# : optAnnotations STRUCT name '{' structFieldList '}'
	# ;

	def __init__(self, _opt_annotations=None, name=None, struct_field_list=None):
		self.opt_annotations = _opt_annotations if _opt_annotations is not None else opt_annotations()
		self.name = name
		self.struct_field_list = struct_field_list

	def randomize(self):
		scope.start_local()
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			self.struct_field_list = struct_field_list(fromObj=self)
			self.struct_field_list.randomize()
			if not self.filter():
				break
		scope.stop_local()
		scope.insert_type(self.name.generate_code(), "struct")

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = self.opt_annotations.generate_code()
		code += 'struct ' + (self.name if isinstance(self.name, basestring) else self.name.generate_code())
		code += ' ' + '{\n' + self.struct_field_list.generate_code() + '}'
		code += '\n\n'
		return code

	def filter(self):
		available_types = scope.get_available_types()
		if self.name.generate_code() in available_types:
			return True
		return False