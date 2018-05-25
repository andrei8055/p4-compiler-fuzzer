from opt_annotations import opt_annotations
from stat_or_decl_list import stat_or_decl_list
from common import common


class block_statement(object):
	type = 'block_statement'
	opt_annotations = None
	stat_or_decl_list = None

	# blockStatement
	# : optAnnotations '{' statOrDeclList '}'
	# ;

	def __init__(self, opt_annotations=None, stat_or_decl_list=None):
		self.opt_annotations = opt_annotations
		self.stat_or_decl_list = stat_or_decl_list

	def randomize(self):
		common.usedRandomize()
		self.opt_annotations = opt_annotations()
		self.opt_annotations.randomize()
		self.stat_or_decl_list = stat_or_decl_list()
		self.stat_or_decl_list.randomize()

	def generate_code(self):
		return self.opt_annotations.generate_code() + '{' + self.stat_or_decl_list.generate_code() + '} '

