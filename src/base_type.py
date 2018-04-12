#!/usr/bin/python
import random
import string

class base_type(object):
	name = ''
	size = None
	type = ''

	def __init__(self, name, size, type):
		self.name = name
		self.size = size
		self.type = type

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def get_type(self):
		return self.type
