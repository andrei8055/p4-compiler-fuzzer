from action_ref import action_ref
from randomizer import randomizer
from common import common


class action_list(object):
	type = 'action_list'
	_action_list = []
	min_list_size = 1
	max_list_size = 5

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, _action_list=None):
		self._action_list = _action_list if _action_list is not None else []

	def randomize(self):
		common.usedRandomize()
		rnd = randomizer.randint(self.min_list_size, self.max_list_size)
		for x in range(0, rnd):
			_action = action_ref()
			_action.randomize()
			self._action_list.append(_action)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _action in self._action_list:
			code += _action.generate_code() + '; '
		return code

