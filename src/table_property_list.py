from table_property import table_property
import random


class table_property_list(object):
	type = 'table_property_list'
	property_list = []
	min_list_size = 1
	max_list_size = 50

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, property_list=[]):
		self.property_list = property_list

	def randomize(self):
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_table_property = table_property()
			_table_property.randomize()
			self.property_list.append(_table_property)

	def generate_code(self):
		code = ''
		for _table_property in self.property_list:
			code += _table_property.generate_code() + ' '
		return code

