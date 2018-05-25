from opt_annotations import opt_annotations
from name import name
from argument_list import argument_list
from common import common


class action_ref(object):
	type = 'action_ref'
	opt_annotations = None
	name = None
	argument_list = None

	# actionRef
	# : optAnnotations name
	# | optAnnotations name '(' argumentList ')'
	# ;

	def __init__(self, opt_annotations=None, name=None, argument_list=None):
		self.opt_annotations = opt_annotations
		self.name = name
		self.argument_list = argument_list

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.name = name()
		self.name.randomize()
		self.argument_list = argument_list()
		self.argument_list.randomize()

	def generate_code(self):
		code = self.opt_annotations.generate_code() + ' ' + self.name.generate_code() + ' '
		if self.argument_list is not None:
			code += '(' + self.argument_list.generate_code() + ')'
