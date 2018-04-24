from identifier_list import identifier_list


class error_declaration(object):
	type = 'error_declaration'

	identifier_list = None

	# errorDeclaration
	# : ERROR '{' identifierList '}'
	# ;

	def __init__(self, identifier_list=None):
		self.identifier_list = identifier_list

	def randomize(self):
		self.identifier_list = identifier_list()
		self.identifier_list.randomize()

	def generate_code(self):
		return 'error ' + ' ' + '{' + self.identifier_list.generate_code() + '}'

