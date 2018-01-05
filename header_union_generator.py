#!/usr/bin/python
from base_type_generator import base_type_generator
from derived_type import derived_type

class header_union_generator(object):
	base_type_generator = base_type_generator()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields, type):
		header_union = derived_type(name, fields, type)
		return header_union

	def generate_random(self, headers):
		name = self.generate_name(headers)
		fields = headers
		type = 'header_union'
		return self.generate(name, fields, type)

	def generate_name(self, headers):
		name = ''
		for header in headers:
			name = name + header.get_name() + '_'
		name = name + 'union'
		return name

	def generate_code(self, header_union):
		code = 'header_union' + ' ' + header_union.get_name() + '{ '
		code = code + self.generate_fields_code(header_union.get_fields())
		code = code + '\n}'
		return code

	def generate_fields_code(self, fields):
		code = ''
		for field in fields:
			code = code + '\n\t'
			code = code + field.get_name()
			code = code + ' '
			code = code + field.get_name()[0].lower() + field.get_name()[1:-2]
		return code
