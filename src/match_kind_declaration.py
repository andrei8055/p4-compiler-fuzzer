from identifier_list import identifier_list
from common import common


class match_kind_declaration(object):
	type = 'match_kind_declaration'

	identifier_list = None

	# matchKindDeclaration
	# : MATCH_KIND  '{' identifierList '}'
	# ;

	def __init__(self, identifier_list=None):
		self.identifier_list = identifier_list

	def randomize(self):
		common.usedRandomize()
		self.identifier_list = identifier_list()
		self.identifier_list.randomize()

	def generate_code(self):
		return 'match_kind ' + ' ' + '{' + self.identifier_list.generate_code() + '}'

