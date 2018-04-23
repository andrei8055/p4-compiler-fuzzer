import random
from common import common

class header_stack(object):
	name = ''
	type = 'header_stack'
	header = None
	size = 0

	common = common()

	name_max_length = 5
	stack_min_size = 1
	stack_max_size = 5

	def __init__(self, name='', header=None, size=0):
		self.name = name
		self.header = header
		self.size = size

	def randomize(self, header):
		self.name = self.generate_name()
		self.size = random.randint(self.stack_min_size, self.stack_max_size)
		self.header = header

	def generate_name(self):
		return self.common.get_random_string(self.name_max_length, False) + '_union'

	def generate_code(self):
		return self.header.get_name() + '[' + str(self.size) + '] ' + self.name + ';'

	def generate_code_ref(self):
		return self.name
