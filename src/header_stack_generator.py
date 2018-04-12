#!/usr/bin/python
import random
from derived_type import derived_type

class header_stack_generator(object):
	name_length = 5
	stack_min_size = 1
	stack_max_size = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, fields, type):
		header_stack = derived_type(name, fields, type, type)
		return header_stack

	def generate_random(self, header):
		name = self.generate_name(header)
		fields = self.generate_fields(random.randint(self.stack_min_size, self.stack_max_size))
		type = header.get_name()
		return self.generate(name, fields, type)

	def generate_fields(self, size):
		fields = [None] * size
		return fields

	def generate_name(self, header):
		code = header.get_name()[0].lower() + header.get_name()[1:-2] + '_stack'
		return code

	def generate_code(self, header_stack):
		return header_stack.get_type() + '[' + str(len(header_stack.get_fields())) + '] ' + header_stack.get_name() + ';'
