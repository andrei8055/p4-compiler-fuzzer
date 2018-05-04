from opt_annotations import opt_annotations
from keyset_expression import keyset_expression
from action_ref import action_ref
from common import common


class entry(object):
	type = 'entry'
	opt_annotations = None
	keyset_expression = None
	action_ref = None

	# entry
	# : optAnnotations keysetExpression ':' actionRef ';'

	def __init__(self, opt_annotations=None, keyset_expression=None, action_ref=None):
		self.opt_annotations = opt_annotations
		self.keyset_expression = keyset_expression
		self.action_ref = action_ref

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.keyset_expression = keyset_expression()
		self.keyset_expression.randomize()
		self.action_ref = action_ref()
		self.action_ref.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' ' + self.keyset_expression.generate_code() + ':' + self.action_ref.generate_code()
