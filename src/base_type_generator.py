#!/usr/bin/python
import random
from common import common
from bool import bool
from varbit import varbit
from void_generator import void
from error import error
from bit import bit
from int import int

class base_type_generator(object):
	common = common()

	base_type_min_size = 1
	base_type_max_size = 1024
	base_type_name_length = 8

	base_types = ['void', 'error', 'match', 'bool', 'bit', 'varbit', 'int']

	def generate_random(self, types):
		size = random.randint(self.base_type_min_size, self.base_type_max_size)
		identifier_list = [] #todo randomize identifier_list
		type = random.choice(self.base_types)

		if len(types) > 0:
			type = random.choice(types)

		if type == 'void':
			return void()
		if type == 'error':
			return error(identifier_list)
		if type == 'bool':
			return bool()
		if type == 'bit':
			return bit(size)
		if type == 'varbit':
			return varbit(size)
		if type == 'int':
			return int(size)
		return None