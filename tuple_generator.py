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

class tuple_generator(object):
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

	def generate(self, name, fields, type):
		tuple = derived_type(name, fields, type, type)
		return tuple

	def generate_random(self, field_types):
		#tuples have no name
		name = ""
		fields = self.generate_fields(field_types)
		type = 'tuple'
		return self.generate(name, fields, type)

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

	def generate_code(self, tuple):
		code = 'tuple ' + '<'
		fields = tuple.get_fields()
		for x in range(0, len(fields)):
			if type(fields[x]).__name__ is 'base_type':
				code = code + self.base_type_generator.generate_code_unnamed(fields[x])
			elif type(fields[x]).__name__ is 'derived_type':
				code = code + fields[x].get_type()
			else:
				code = code + 'UNKNOWN_TYPE UNKNOWN_NAME'
			if x < len(fields) - 1:
				code = code + ', '
		code = code + '> '
		code = code + self.common.get_random_string(self.name_length, True) + '= {'
		for x in range(0, len(fields)):
			if type(fields[x]).__name__ is 'base_type':
				code = code + '1'
			elif type(fields[x]).__name__ is 'derived_type':
				code = code + '2'
			else:
				code = code + 'UNKNOWN_TYPE UNKNOWN_NAME'
			if x < len(fields) - 1:
				code = code + ', '
		code = code + '}; '
		return code

