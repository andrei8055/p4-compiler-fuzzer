from expression_list import expression_list
from select_case_list import select_case_list
from common import common


class select_expression(object):
	type = 'select_expression'
	expression_list = None
	select_case_list = None

	# selectExpression
	# : SELECT '(' expressionList ')' '{'selectCaseList '}'
	# ;

	def __init__(self, expression_list=None, select_case_list=None):
		self.expression_list = expression_list
		self.select_case_list = select_case_list

	def randomize(self):
		common.usedRandomize()
		self.expression_list = expression_list()
		self.expression_list.randomize()
		self.select_case_list = select_case_list()
		self.select_case_list.randomize()

	def generate_code(self):
		return 'select(' + self.expression_list.generate_code() + ') { ' + self.select_case_list.generate_code() + ' } '
