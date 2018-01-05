#!/usr/bin/python
import random
from base_type import base_type

class header_stack_generator(object):
	name_length = 5
	stack_min_size = 1
	stack_max_size = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, name, size, type):
		header_stack = base_type(name, size, type)
		return header_stack

	def generate_random(self, header):
		name = self.generate_name(header)
		size = self.generate_size()
		type = 'header_stack'
		return self.generate(name, size, type)

	def generate_size(self):
		return random.randint(self.stack_min_size, self.stack_max_size)

	def generate_name(self, header):
		code = header.get_name()[0].lower() + header.get_name()[1:-2] + '_stack'
		return code

	def generate_code(self, header_stack):
		return header_stack.get_type() + '[' + str(header_stack.get_size()) + '] ' + header_stack.get_name() + ';'
