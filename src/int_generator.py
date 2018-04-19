#!/usr/bin/python
from common import common
from int import int

class int_generator(object):
	common = common()

	def generate(self, size):
		return int(size)

	def generate_random(self):
		size = 1 #todo randomize
		return self.generate(size)




