from table_property import table_property
from randomizer import randomizer
from common import common


class table_property_list(object):
	type = 'table_property_list'
	property_list = []

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, property_list=None):
		self.property_list = property_list if property_list is not None else []

	def randomize(self):
		_table_property = table_property(force_type=0)
		_table_property.randomize()
		self.property_list.append(_table_property)
		_table_property = table_property(force_type=1)
		_table_property.randomize()
		self.property_list.append(_table_property)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _table_property in self.property_list:
			code += _table_property.generate_code() + '\n'
		return code

