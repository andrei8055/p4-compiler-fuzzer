from opt_annotations import opt_annotations
from name import name
from struct_field_list import struct_field_list
from common import common
from scope import scope


class header_union_declaration(object):
	type = 'header_union_declaration'

	opt_annotations = None
	name = None
	struct_field_list = None

	# headerUnionDeclaration
	# : optAnnotations HEADER_UNION name '{' structFieldList '}'
	# ;

	def __init__(self, opt_annotations=None, name=None, struct_field_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.struct_field_list = struct_field_list

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.name = name()
		self.name.randomize()
		self.struct_field_list = struct_field_list()
		self.struct_field_list.randomize()
		scope.insert_type(name.generate_code(), "header_union")

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' header_union ' + self.name.generate_code() + ' ' + '{' + self.struct_field_list.generate_code() + '}'
