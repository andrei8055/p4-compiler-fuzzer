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
		return base_type(name, size, type)

	def generate_random_base_type(self, types):
		size = random.randint(self.base_type_min_size, self.base_type_max_size)
		name = self.common.get_random_string(self.base_type_name_length, True)
		if types:
			type = random.choice(types)
		else:
			type = random.choice(self.base_types)

		if type == 'void':
			return self.generate_base_type(name, None, 'void')
		elif type == 'error':
			return self.generate_base_type(name, None, 'error')
		elif type == 'match_kind':
			return self.generate_base_type(name, None, 'match_kind')
		elif type == 'bool':
			return self.generate_base_type(name, None, 'bool')
		elif type == 'bit':
			return self.generate_base_type(name, size, 'bit')
		elif type == 'sint':
			return self.generate_base_type(name, size, 'int')
		elif type == 'varbit':
			return self.generate_base_type(name, size, 'varbit')
		elif type == 'int':
			return self.generate_base_type(name, size, 'int')
		else:
			return self.generate_base_type(name, None, 'UNKNOWN')