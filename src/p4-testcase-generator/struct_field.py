from opt_annotations import opt_annotations
from type_ref import type_ref
from name import name
from scope import scope
from common import common


class struct_field(object):
	type = 'structField'

	opt_annotations = None
	type_ref = None
	name = None

	fromObj = None

	header_banned_types = ["struct", "header", "bool", "error", "varbit"]

	# structField
	# : optAnnotations typeRef name';'
	# ;

	def __init__(self, opt_annotations=None, type_ref=None, name=None, fromObj=None):
		self.opt_annotations = opt_annotations
		self.type_ref = type_ref
		self.name = name
		self.fromObj = fromObj

	def get_type(self):
		return self.type

	def randomize(self):
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.type_ref = type_ref()
			self.type_ref.randomize()
			self.name = name()
			self.name.randomize()
			if not self.filter():
				break
		scope.insert_variable(self.name.generate_code(), self.type_ref.get_ref_type(), self)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = self.opt_annotations.generate_code()
		code += self.type_ref.generate_code() + ' '
		code += self.name.generate_code() + ';'
		return code

	def filter(self):
		from header_type_declaration import header_type_declaration
		from struct_type_declaration import struct_type_declaration
		if self.type_ref.get_type() == 'specializedType':
			return True
		if self.type_ref.get_type() == 'headerStackType':
			return True
		if self.name.generate_code() in scope.get_available_types() or self.name.generate_code() in scope.get_available_variables():
			return True
		if isinstance(self.fromObj, header_type_declaration):
			if self.type_ref.get_ref_type() in self.__class__.header_banned_types:
				return True
		return False

