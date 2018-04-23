from common import common
from annotation import annotation
import random
import sys


class table_actions(object):
	action_elements = None
	type = 'table_key'

	name_min_length = 1
	name_max_length = 50
	common = common()

	def __init__(self, action_elements=None):
		self.action_elements = action_elements

	def get_action_elements(self):
		return self.action_elements

	def get_type(self):
		return self.type

	def randomize(self):
		pass

	#  ACTIONS '=' '{' actionList '}'
	def generate_code(self):
		code = ''
		code += 'actions = { \n'
		for action in self.action_elements:
			code += str(action.generate_code_ref(self.action_elements[action])) + ';'
			code += '\n'
		code += '\n} \n'
		return code