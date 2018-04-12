#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from derived_type import derived_type
from common import common

class header_generator(object):
	common = common()
	base_type_generator = base_type_generator()
	name_length = 15
	field_name_length = 15
	field_min_number = 1
	field_max_number = 15

	def generate(self, name, fields):
		type = 'header'
		header = derived_type(name, fields, type, type)
		return header

	def generate_random(self):
		name = self.generate_name()
		fields = self.generate_fields()
		return self.generate(name, fields)

	def generate_fields(self):
		varbit_exist = False
		number_of_fields = random.randint(self.field_min_number, self.field_max_number)
		field_list = []
		for x in range(0, number_of_fields):
			if not varbit_exist:
				field = self.generate_field(['bit', 'int', 'varbit'])
				if field.get_type() == 'varbit':
					varbit_exist = True
			else:
				field = self.generate_field(['bit', 'int'])
			field_list.append(field)
		return field_list

	def generate_field(self, types):
		field = self.base_type_generator.generate_random_base_type(types)
		return field

	def generate_name(self):
		return self.common.get_random_string(self.name_length, True) + '_h'

	def generate_code(self, header):
		code = 'header' + ' ' + header.get_name() + '{ '
		for field in header.get_fields():
			code = code + '\n\t' + self.base_type_generator.generate_code(field) + ';'
		code = code + '\n}'
		return code


