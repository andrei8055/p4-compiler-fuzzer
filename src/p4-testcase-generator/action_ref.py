from opt_annotations import opt_annotations
from argument_list import argument_list
from common import common
from randomizer import randomizer
from scope import scope


class action_ref(object):
	type = None
	types = ["name", "nameArgumentList"]
	probabilities = [100, 0]

	opt_annotations = None
	name = None
	argument_list = None

	force_action = None

	# actionRef
	# : optAnnotations name
	# | optAnnotations name '(' argumentList ')'
	# ;

	def __init__(self, opt_annotations=None, name=None, argument_list=None, force_action=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.argument_list = argument_list
		self.force_action = force_action

	def randomize(self):
		common.usedRandomize()
		self.type = randomizer.getRandom(self.probabilities)
		if self.type == 0:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			available_actions = scope.get_available_actions()
			rnd_action = randomizer.randint(0, len(available_actions) - 1)
			if self.force_action is not None:
				rnd_action = self.force_action
			self.name = available_actions.keys()[rnd_action]
		else:
			self.opt_annotations = opt_annotations()
			self.opt_annotations.randomize()
			available_actions = scope.get_available_actions()
			rnd_action = randomizer.randint(0, len(available_actions) - 1)
			if self.force_action is not None:
				rnd_action = self.force_action
			self.name = available_actions.keys()[rnd_action]
			self.argument_list = argument_list()
			self.argument_list.randomize()

	def generate_code(self):
		common.usedCodeGenerator(self)
		code = self.opt_annotations.generate_code() + ' ' + self.name + ' '
		if self.argument_list is not None:
			code += '(' + self.argument_list.generate_code() + ')'
		return code
