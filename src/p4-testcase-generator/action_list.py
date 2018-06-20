from action_ref import action_ref
from randomizer import randomizer
from common import common
from scope import scope


class action_list(object):
	type = 'action_list'
	_action_list = []

	# tablePropertyList
	# : tableProperty
	# | tablePropertyList tableProperty
	# ;

	def __init__(self, _action_list=None):
		self._action_list = _action_list if _action_list is not None else []

	def randomize(self):
		common.usedRandomize()
		rnd = randomizer.randint(0, len(scope.get_available_actions())-1)
		for x in range(0, rnd):
			_action = action_ref(force_action=x)
			_action.randomize()
			self._action_list.append(_action)

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = ''
		for _action in self._action_list:
			code += _action.generate_code() + '; '
		return code

