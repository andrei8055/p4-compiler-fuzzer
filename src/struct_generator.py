#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from base_type import base_type
from derived_type import derived_type
from common import common
from enum_generator import enum_generator
from header_generator import header_generator
from header_union_generator import header_union_generator
from header_stack_generator import header_stack_generator

class struct_generator(object):
	common = common()
	enum_generator = enum_generator()
	header_generator = header_generator()
	header_union_generator = header_union_generator()
	header_stack_generator = header_stack_generator()
	base_type_generator = base_type_generator()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields):
		type = 'struct'
		struct = derived_type(name, fields, type, type)
		return struct

	def generate_random(self, field_types):
		name = self.generate_name()
		fields = self.generate_fields(field_types)
		return self.generate(name, fields)

	def generate_name(self):
		return self.common.get_random_string(self.name_length, True) + '_struct'

	def generate_fields(self, field_types):
		field_list = []
		for random_type in field_types:
			field = None
			if type(random_type) is str:
				field = self.base_type_generator.generate_specific_base_type(random_type)
			elif type(random_type).__name__ is 'derived_type':
				_type = random_type.get_name()
				base_type = random_type.get_base_type()
				name = self.common.get_random_string(5, False) + '_' + _type.lower()
				fields = random_type.get_fields()
				field = derived_type(name, fields, _type, base_type)
			else:
				pass
			if field:
				field_list.append(field)
		return field_list

	def generate_code(self, struct):
		code = 'struct' + ' ' + struct.get_name() + '{ '
		for field in struct.get_fields():
			if type(field).__name__ is 'base_type':
				code = code + '\n\t' + self.base_type_generator.generate_code(field) + ';'
			elif type(field).__name__ is 'derived_type':
				code = code + '\n\t' + field.get_type() + ' ' + field.get_name() + ';'
			else:
				code = code + '\n\t' + 'UNKNOWN_TYPE UNKNOWN_NAME'
		code = code + '\n}'
		return code
