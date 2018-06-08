from struct_field import struct_field
from randomizer import randomizer
from common import common


class struct_field_list(object):
	field_list = []
	min_list_size = 1
	max_list_size = 30

	type = None
	types = ["empty", "structFieldList"]
	probabilities = [50,50]

	fromObj = None

	# structFieldList
	# : / *empty * /
	# | structFieldList structField
	# ;

	def __init__(self, field_list=None, fromObj=None):
		self.field_list = field_list if field_list is not None else []
		self.fromObj = fromObj

	def getType(self):
		return self.types[self.type]

	def randomize(self):
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.field_list = []
		else:
			rndl = randomizer.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_struct_field = struct_field(fromObj=self.fromObj)
				_struct_field.randomize()
				self.field_list.append(_struct_field)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _struct_field in self.field_list:
			code += _struct_field.generate_code() + '\n'
		return code

