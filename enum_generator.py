#!/usr/bin/python
import random
from common import common
from derived_type import derived_type

class enum_generator(object):
	common = common()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields, type):
		enum = derived_type(name, fields, type)
		return enum

	def generate_random(self):
		name = self.generate_name()
		fields = self.generate_fields(random.randint(self.field_min_number, self.field_max_number))
		type = 'enum'
		return self.generate(name, fields, type)

	def generate_fields(self, number):
		fields = []
		for x in range(0, number):
			fields.append(self.common.get_random_string(self.field_name_length, True))
		return fields

	def generate_name(self):
		code = self.common.get_random_string(self.name_length, True) + '_enum'
		return code

	def generate_code(self, enum):
		return 'enum' + ' ' + enum.get_name() + ' ' + '{' + self.generate_fields_code(enum.get_fields()) + '}'

	def generate_fields_code(self, fields):
		return ', '.join(fields)
