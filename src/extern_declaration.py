from randomizer import randomizer
from extern_declaration_method import extern_declaration_method
from extern_declaration_function import extern_declaration_function


class extern_declaration(object):
	type = 'extern_declaration'
	value = None

	# externDeclaration
	# : optAnnotations EXTERN nonTypeName optTypeParameters '{' methodPrototypes '}'
	# | optAnnotations EXTERN functionPrototype ';'
	# ;

	def __init__(self, value=None):
		self.value = value

	def randomize(self):
		rnd = randomizer.randint(0, 1)
		if rnd == 0:
			self.value = extern_declaration_method()
		elif rnd == 1:
			self.value = extern_declaration_function()
		self.value.randomize()

	def generate_code(self):
		return self.value.generate_code()
