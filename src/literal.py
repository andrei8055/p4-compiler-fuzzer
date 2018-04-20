from common import common
import random


class literal(object):

    #  todo generated bit, varbit values
    @staticmethod
    def get(type):
        _common = common()
        max_string_length = 1000
        max_int_size = 100000

        # if type == 'error':
        #     return error(identifier_list)
        if type.get_name() == 'bool':
            return random.choice(["true", "false"])
        if type.get_name() == 'bit':
            return '"' + _common.get_random_string(type.get_size(), False) + '"'
        if type.get_name() == 'varbit':
            return '"' + bin(_common.get_random_number(0, type.get_size())) + '"'
        if type.get_name() == 'int':
            return _common.get_random_number(0, type.get_size())
        return ''

