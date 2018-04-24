from statement_or_declaration import statement_or_declaration
import random


class stat_or_decl_list(object):
	type = 'stat_or_decl_list'
	list = []
	min_list_size = 1
	max_list_size = 50

	# statOrDeclList
	# : / *empty * /
	# | statOrDeclList statementOrDeclaration
	# ;


	def __init__(self, list=[]):
		self.list = list

	def randomize(self):
		rnd = random.randint(0, 1)
		if rnd == 0:
			self.list = []
		else:
			rndl = random.randint(self.min_list_size, self.max_list_size)
			for x in range(0, rndl):
				_statement_or_declaration = statement_or_declaration()
				_statement_or_declaration.randomize()
				self.list.append(_statement_or_declaration)

	def generate_code(self):
		code = ''
		for _statement_or_declaration in self.list:
			code += _statement_or_declaration.generate_code() + ' '
		return code
