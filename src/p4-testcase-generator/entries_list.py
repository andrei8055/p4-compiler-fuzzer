from entry import entry
from randomizer import randomizer
from common import common


class entries_list(object):
	type = 'entries_list'
	entry_list = []
	min_list_size = 1
	max_list_size = 5

	# entriesList
	# : entry
	# | entryList entry

	def __init__(self, entry_list=None):
		self.entry_list = entry_list if entry_list is not None else []

	def randomize(self):
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_entry = entry()
			_entry.randomize()
			self.entry_list.append(_entry)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _entry in self.entry_list:
			code += _entry.generate_code() + ' '
		return code

