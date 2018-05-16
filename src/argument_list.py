from non_empty_arg_list import non_empty_arg_list
from randomizer import randomizer
from common import common


class argument_list(object):
	type = 'argument_list'
	non_empty_arg_list = None

	# argumentList
	# : / *empty * /
	# | nonEmptyArgList
	# ;

	def __init__(self, non_empty_arg_list=None):
		self.non_empty_arg_list = non_empty_arg_list

	def randomize(self):
		common.usedRandomize()
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.non_empty_arg_list = None
		else:
			self.non_empty_arg_list = non_empty_arg_list()
			self.non_empty_arg_list.randomize()

	def generate_code(self):
		if self.non_empty_arg_list is not None:
			return self.non_empty_arg_list.generate_code()
		else:
			return ''

