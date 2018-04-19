#!/usr/bin/python
from common import common
from void import void

class void_generator(object):
	common = common()

	def generate(self):
		return void()

	def generate_random(self):
		return self.generate()

	def generate_code(self, void):
		return void.get_name()




