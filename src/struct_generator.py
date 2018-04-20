#!/usr/bin/python
import random
from base_type_generator import base_type_generator
from derived_type import derived_type
from common import common
from struct import struct

class struct_generator(object):
	common = common()
	base_type_generator = base_type_generator()
	name_length = 5
	field_name_length = 5
	field_min_number = 1
	field_max_number = 5

	def generate(self, annotation, name, fields):
		return struct(annotation, name, fields)

	# def generate_random(self):
	# 	annotation = self.annotation_generator.generate_random()
	# 	name = self.generate_name()
	# 	fields = self.generate_fields()
	# 	return self.generate(annotation, name, fields)

	def generate_name(self):
		return self.common.get_random_string(self.name_length, True) + '_struct'

	# def generate_fields(self, field_types):
	# 	field_list = []
	# 	for random_type in field_types:
	# 		field = None
	# 		if type(random_type) is str:
	# 			field = self.base_type_generator.generate_specific_base_type(random_type)
	# 		elif type(random_type).__name__ is 'derived_type':
	# 			_type = random_type.get_name()
	# 			base_type = random_type.get_base_type()
	# 			name = self.common.get_random_string(5, False) + '_' + _type.lower()
	# 			fields = random_type.get_fields()
	# 			field = derived_type(name, fields, _type, base_type)
	# 		else:
	# 			pass
	# 		if field:
	# 			field_list.append(field)
	# 	return field_list

	def generate_code(self, struct):
		code = 'struct' + ' ' + struct.get_name() + '{ '
		code = code + '\n}'
		return code

