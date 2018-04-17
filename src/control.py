#!/usr/bin/python
class control(object):
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-control
	name = ''
	type = ''
	parameters = []
	declarations = []

	def __init__(self, name, parameters, declarations):
		self.name = name
		self.type = 'parser'
		self.parameters = parameters
		self.declarations = declarations

	def get_name(self):
		return self.name

	def get_parameters(self):
		return self.parameters

	def get_declarations(self):
		return self.declarations

	def get_type(self):
		return self.type

