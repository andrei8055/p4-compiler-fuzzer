#!/usr/bin/python
class parser(object):
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-parser-decl
	name = ''
	type = ''
	parameters = []
	#local_elements = '' TODO add
	states = []

	def __init__(self, name, parameters, states):
		self.name = name
		self.type = 'parser'
		self.parameters = parameters
		self.states = states

	def get_name(self):
		return self.name

	def get_parameters(self):
		return self.parameters

	def get_states(self):
		return self.states

	def get_type(self):
		return self.type

