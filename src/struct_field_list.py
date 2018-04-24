from struct_field import struct_field
import random


class struct_field_list(object):
	type = 'struct_field_list'
	field_list = []
	min_list_size = 1
	max_list_size = 50

	# structFieldList
	# : / *empty * /
	# | structFieldList structField
	# ;

	def __init__(self, field_list=[]):
		self.field_list = field_list

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.field_list = []
		else:
			rndl = random.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_struct_field = struct_field()
				_struct_field.randomize()
				self.field_list.append(_struct_field)

	def generate_code(self):
		code = ''
		for _struct_field in self.field_list:
			code += _struct_field.generate_code() + ' '
		return code

