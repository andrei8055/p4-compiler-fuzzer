#!/usr/bin/python
import random
import string
from common import common
from base_type import base_type

class base_type_generator(object):
	common = common()
	base_type_min_size = 2
	base_type_max_size = 4
	base_type_name_length = 5

	base_types = ['void', 'error', 'match', 'bool', 'bit', 'sint', 'varbit', 'int']

	def generate_base_type(self, name, size, type):
		_type = type
		if(_type) not in self.base_types:
			_type = 'UNKNOWN'
		return base_type(name, size, _type)

	def generate_random_base_type(self):
		size = random.randint(self.base_type_min_size, self.base_type_max_size)
		name = self.common.get_random_string(self.base_type_name_length, True)
		type = random.choice(self.base_types)

		if type in ['bit', 'int', 'varbit']:
			return self.generate_base_type(name, size, type)
		else:
			return self.generate_base_type(name, None, type)

	def generate_specific_base_type(self, type):
		name = self.common.get_random_string(self.base_type_name_length, True)

		if type in ['bit', 'int', 'varbit']:
			size = random.randint(self.base_type_min_size, self.base_type_max_size)
			return self.generate_base_type(name, size, type)
		else:
			return self.generate_base_type(name, None, type)

	def generate_code(self, base_type):
		if base_type.get_type() in ['bit', 'int', 'varbit']:
			return base_type.get_type() + '<' + str(base_type.get_size()) + '>' + ' ' + base_type.get_name()
		else:
			return base_type.get_type() + ' ' + base_type.get_name()
