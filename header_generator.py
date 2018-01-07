#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from derived_type import derived_type
from common import common

class header_generator(object):
	common = common()
	base_type_generator = base_type_generator()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields, type):
		header = derived_type(name, fields, type, type)
		return header

	def generate_random(self):
		name = self.generate_name()
		fields = self.generate_fields()
		type = 'header'
		return self.generate(name, fields, type)

	def generate_fields(self):
		number_of_fields = random.randint(self.field_min_number, self.field_max_number)
		field_list = []
		for x in range(0, number_of_fields):
			field_list.append(self.generate_field())
		return field_list

	def generate_field(self):
		field = self.base_type_generator.generate_random_base_type()
		return field

	def generate_name(self):
		return self.common.get_random_string(self.name_length, True) + '_h'

	def generate_code(self, header):
		code = 'header' + ' ' + header.get_name() + '{ '
		for field in header.get_fields():
			code = code + '\n\t' + self.base_type_generator.generate_code(field)
		code = code + '\n}'
		return code


