#!/usr/bin/python
class derived_type(object):
	name = ''
	fields = []
	type = ''

	def __init__(self, name, fields, type):
		self.name = name
		self.fields = fields
		self.type = type

	def get_name(self):
		return self.name

	def get_size(self):
		return len(self.fields)

	def get_fields(self):
		return self.fields

	def get_type(self):
		return self.type