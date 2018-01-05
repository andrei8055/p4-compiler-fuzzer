#!/usr/bin/python
from base_type_generator import base_type_generator
from base_type import base_type
from derived_type import derived_type
from common import common

class struct_generator(object):
	common = common()
	base_type_generator = base_type_generator()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields, type):
		struct = derived_type(name, fields, type)
		return struct

	def generate_random(self, field_list):
		name = self.generate_name()
		fields = field_list
		type = 'struct'
		return self.generate(name, fields, type)

	def generate_name(self):
		return self.common.get_random_string(self.name_length, True) + '_struct'

	def generate_code(self, struct):
		code = 'struct' + ' ' + struct.get_name() + '{ '
		for field in struct.get_fields():
			if type(field) is base_type:
				code = code + self.generate_base_type_field_code(field)
			elif type(field) is derived_type:
				code = code + self.generate_derived_type_field_code(field)
			else:
				code = code + 'UNKNOWN' + '\n'

		code = code + '\n}'
		return code

	def generate_base_type_field_code(self, field):
		code = ''
		code = code + '\n\t'
		code = code + field.get_type()
		code = code + ' '
		if field.get_size() is not None:
			code = code + '<' + str(field.get_size()) + '>'
		code = code + ' '
		code = code + field.get_name()
		return code

	def generate_derived_type_field_code(self, field):
		code = ''
		code = code + '\n\t'
		code = code + field.get_name()
		code = code + ' '
		code = code + field.get_name()[0].lower() + field.get_name()[1:-2]
		return code
