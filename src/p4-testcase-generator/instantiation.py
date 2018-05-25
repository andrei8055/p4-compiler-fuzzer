from opt_annotations import opt_annotations
from type_ref import type_ref
from argument_list import argument_list
from name import name
from common import common


class instantiation(object):
	opt_annotations = None
	type_ref = None
	argument_list = None
	name = None
	type = 'instantiation'

	# instantiation
	# 	: opt_annotations typeRef '(' argumentList ')' name
	# 	';'
	#
	# * replaced empty and annotation rules with opt_annotation in original

	def __init__(self, opt_annotations=None, type_ref=None, argument_list=None, name=None):
		self.opt_annotations = opt_annotations
		self.type_ref = type_ref
		self.argument_list = argument_list
		self.name = name

	def get_name(self):
		return self.name

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.name = name()
		self.name.randomize()
		self.type_ref = type_ref()
		self.type_ref.randomize()
		self.argument_list = argument_list()
		self.argument_list.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + ' ' + self.type_ref.generate_code() + ' (' + self.argument_list.generate_code() + ') ' + self.name.generate_code() + ';'
