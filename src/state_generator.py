from state import state

class state_generator(object):
	
	def generate(self, name, transitions):
		return state(name, transitions, 'state')

	def generate_code(self, state):
		code = 'state' + ' ' + str(state.get_name()) + ' ' + '{ \n'
		code = code + '\n transition accept;' #todo generate state body
		code = code + '} \n'
		return code
