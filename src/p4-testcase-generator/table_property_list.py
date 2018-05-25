from table_property import table_property
from randomizer import randomizer


class table_property_list(object):
	type = 'table_property_list'
	property_list = []
	min_list_size = 1
	max_list_size = 5

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, property_list=None):
		self.property_list = property_list if property_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_table_property = table_property()
			_table_property.randomize()
			self.property_list.append(_table_property)

	def generate_code(self):
		code = ''
		for _table_property in self.property_list:
			code += _table_property.generate_code() + ' '
		return code

