from opt_annotations import opt_annotations
from name import name
from table_property_list import table_property_list


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
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.name = name()
		self.name.randomize()
		self.table_property_list = table_property_list()
		self.table_property_list.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' table ' + self.name.generate_code() + ' ' + '{' + self.table_property_list.generate_code() + '}'
