#!/usr/bin/python
class myparser(object):
	#https://p4.org/p4-spec/docs/P4-16-v1.0.0-spec.html#sec-parser-decl
	name = ''
	type = ''
	parameters = []
	constants = []
	variables = []
	states = []

	def __init__(self, name, parameters, constants, variables, states):
		self.name = name
		self.type = 'parser'
		self.parameters = parameters
		self.constants = constants
		self.variables = variables
		self.states = states

	def get_name(self):
		return self.name

	def get_parameters(self):
		return self.parameters

	def get_constants(self):
		return self.constants

	def get_variables(self):
		return self.variables

	def get_states(self):
		return self.states

	def get_type(self):
		return self.type

