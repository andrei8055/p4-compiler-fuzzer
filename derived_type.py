#!/usr/bin/python
import random
import string
from base_type import base_type

class derived_type:
	types = ['enum', 'header', 'header_stacks', 'struct', 'header_union', 'tuple', 'type_specialization', 'extern',
			 'parser', 'control', 'package']
	bt = base_type()
	header_list = []
	header_stacks_list = []
	header_union_list = []

	def get_enum(self, n):
		identifiers = []
		number = n
		if number == -1:
			number = random.randint(2, 4)
		for x in range(0, number):
			identifiers.append(self.get_random_name(True))
		return 'enum' + ' ' + self.get_random_name(True) + ' ' + '{' + ','.join(identifiers) + '}'

	################
	# HEADER TYPES #
	################

	def get_header_type_declaration(self):
		header_name = self.get_header_name()
		while header_name in self.header_list:
			header_name = self.get_header_name()
		self.header_list.append(header_name)
		return self.get_header() + ' ' + header_name + self.get_struct_field_list()

	def get_header(self):
		return 'header'

	def get_header_name(self):
		return self.get_random_name(True) + '_h'

	def get_struct_field_list(self):
		list_size = random.randint(2, 4)
		struct_field_list = []
		for x in range(0, list_size):
			struct_field_list.append(self.get_struct_field())
		return '{ \n \t' + '; \n \t'.join(struct_field_list) + ';' + '\n}'

	def get_struct_field(self):
		field_size = random.randint(2, 4)
		name = self.get_random_name(True)
		type = self.bt.get_random_type(['bit', 'varbit'], field_size)
		return type + ' ' + name

	def get_header_list(self):
		return self.header_list

	#################
	# HEADER STACKS #
	#################

	def get_header_stack(self, header):
		stack_size = random.randint(2, 4)
		stack_name = header[0].lower() + header[1:-2] + '_stack'
		stack_type = header
		if stack_name not in self.header_stacks_list:
			hs = header_stack(stack_name, stack_size, stack_type)
			self.header_stacks_list.append(hs)
			return hs.get_type() + '[' + str(hs.get_size()) + '] ' + hs.get_name() + ';'
		else:
			return ''

	def get_header_stack_list(self):
		return self.header_stacks_list

	#################
	# HEADER UNIONS #
	#################

	def get_header_union_declaration(self, headers):
		union_size = len(headers)
		union_types = headers
		union_name = '_'.join(headers)+'_union'
		if union_name not in self.header_union_list:
			hu = header_union(union_name, union_size, union_types)
			self.header_union_list.append(hu)
			declaration = 'header_union' + ' ' + hu.get_name() + '{ \n\t'
			for type in hu.get_types():
				declaration = declaration + type + ' ' + type[0].lower() + type[1:-2] + '; \n\t'
			declaration = declaration + '\n}'
			return declaration
		else:
			return ''


	###########
	# STRUCTS #
	###########

	def get_struct(self):
		return 1

	def get_random_name(self, first_capital):
		name_length = 5
		if first_capital:
			return ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length)).capitalize()
		else:
			return ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length))


class header_stack:
	name = ''
	size = 0
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


class header_union:
	name = ''
	size = 0
	types = []

	def __init__(self, name, size, types):
		self.name = name
		self.size = size
		self.types = types

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def get_types(self):
		return self.types