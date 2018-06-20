from opt_annotations import opt_annotations
from name import name
from table_property_list import table_property_list
from common import common
from scope import scope


class table_declaration(object):
	type = 'table_declaration'

	opt_annotations = None
	name = None
	table_property_list = None

	# tableDeclaration
	# : optAnnotations TABLE name '{' tablePropertyList '}'
	# ;

	def __init__(self, opt_annotations=None, name=None, table_property_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.table_property_list = table_property_list

	def randomize(self):
		common.usedRandomize()
		while True:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			self.name = name()
			self.name.randomize()
			self.table_property_list = table_property_list()
			self.table_property_list.randomize()
			if not self.filter():
				break

	def filter(self):
		if self.name.generate_code() in scope.get_available_types():
			return True
		if self.name.generate_code() in scope.get_available_variables():
			return True
		if self.name.generate_code() in scope.get_available_states():
			return True
		if self.name.generate_code() in scope.get_available_actions():
			return True
		if self.name.generate_code() in scope.get_available_tables():
			return True
		return False

	def generate_code(self):
		common.usedCodeGenerator(self)
		return self.opt_annotations.generate_code() + 'table ' + self.name.generate_code() + ' ' + '{\n\n' + self.table_property_list.generate_code() + '\n}\n\n'
