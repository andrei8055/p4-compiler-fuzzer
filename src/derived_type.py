#!/usr/bin/python
class derived_type(object):
	name = ''
	fields = []
	type = ''
	base_type = ''

	def __init__(self, name, fields, type, base_type):
		self.name = name
		self.fields = fields
		self.type = type
		self.base_type = base_type

	def get_name(self):
		return self.name

	def get_size(self):
		return len(self.fields)

	def get_fields(self):
		return self.fields

	def get_type(self):
		return self.type
		
	def get_base_type(self):
		return self.base_type
