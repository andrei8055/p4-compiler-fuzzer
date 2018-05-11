from struct_field import struct_field
from randomizer import randomizer
import random


class struct_field_list(object):
	field_list = []
	min_list_size = 1
	max_list_size = 5

	type = None
	types = ["empty", "structFieldList"]
	probabilities = [5,5]

	# structFieldList
	# : / *empty * /
	# | structFieldList structField
	# ;

	def __init__(self, field_list=[]):
		self.field_list = field_list

	def getType(self):
		return self.types[self.type]

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.field_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_struct_field = struct_field()
				_struct_field.randomize()
				self.field_list.append(_struct_field)

	def generate_code(self):
		code = ''
		for _struct_field in self.field_list:
			code += _struct_field.generate_code() + ' '
		return code

