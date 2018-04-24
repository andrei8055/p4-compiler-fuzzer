import random
from base_type import base_type
from type_name import type_name
from specialized_type import specialized_type
from header_stack_type import header_stack_type


class type_ref(object):
	type = 'type_ref'
	value = None

	# typeRef
	# : baseType
	# | typeName
	# | specializedType
	# | headerStackType
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = random.randint(0, 3)
		if rnd == 0:
			self.value = base_type()
		elif rnd == 1:
			self.value = type_name()
		elif rnd == 2:
			self.value = specialized_type()
		elif rnd == 3:
			self.value = header_stack_type()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
