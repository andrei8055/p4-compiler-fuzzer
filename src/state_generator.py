from common import common
from state import state

class state_generator(object):
	common = common()
	
	def generate(self, name, body):
		return state(name, body, 'state')

	def generate_code(self, state):
		code = 'state' + ' ' + str(state.get_name()) + ' ' + '{ \n'
		code = code + str(state.get_body())
		code = code + '} \n'
		return code
