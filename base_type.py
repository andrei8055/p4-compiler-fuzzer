#!/usr/bin/python
import random

class base_type:

    types = ['void', 'error', 'match_kind', 'bool', 'bit', 'sint', 'varbit', 'int']
    def get_void(self):
        return 'void'

    def get_error(self):
        return 'error'

    def get_match_kind(self):
        return 'match_kind'

    def get_bool(self):
        return 'bool'

    def get_bit(self, s):
        return 'bit<%d>' % s

    def get_sint(self, s):
        return 'int<%d>' % s

    def get_varbit(self, s):
        return 'varbit<%d>' % s

    def get_int(self):
        return 'int'

    def get_random_type(self, l, s):
		if l:
			type = random.choice(l)
		else:
			type = random.choice(self.types)
		if type == 'void':
			return self.get_void()
		elif type == 'error':
			return self.get_error()
		elif type == 'match_kind':
			return self.get_match_kind()
		elif type == 'bit':
			return self.get_bit(s)
		elif type == 'sint':
			return self.get_sint(s)
		elif type == 'varbit':
			return self.get_varbit(s)
		else:
			return self.get_int()

