from lvalue import lvalue
from type_argument_list import type_argument_list
from argument_list import argument_list


class method_call_statement(object):
	type = 'method_call_statement'
	lvalue = None
	type_argument_list = None
	argument_list = None

	# : lvalue '(' argumentList ')' ';'
	# | lvalue '<'typeArgumentList'>' '('argumentList ')' ';'

	def __init__(self, lvalue=None, type_argument_list=None, argument_list=None):
		self.lvalue = lvalue
		self.type_argument_list = type_argument_list
		self.argument_list = argument_list

	def randomize(self):
		self.lvalue = lvalue()
		self.lvalue.randomize()
		self.type_argument_list = type_argument_list()
		self.type_argument_list.randomize()
		self.argument_list = argument_list()
		self.argument_list.randomize()

	def generate_code(self):
		code = ''
		code += self.lvalue.generate_code() + ' '
		if self.type_argument_list is not None:
			code += '<' + self.type_argument_list.generate_code() + '>'
			code += '(' + self.argument_list.generate_code() + ')'
		return code

