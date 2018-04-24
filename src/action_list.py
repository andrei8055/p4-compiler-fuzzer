from action_ref import action_ref
import random


class action_list(object):
	type = 'action_list'
	_action_list = []
	min_list_size = 1
	max_list_size = 50

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, _action_list=[]):
		self._action_list = _action_list

	def randomize(self):
		rnd = random.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_action = action_ref()
			_action.randomize()
			self._action_list.append(_action)

	def generate_code(self):
		code = ''
		for _action in self._action_list:
			code += _action.generate_code() + '; '
		return code

