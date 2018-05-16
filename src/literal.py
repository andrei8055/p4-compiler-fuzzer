from common import common
from randomizer import randomizer


class literal(object):

    #  todo generated bit, varbit values
    @staticmethod
    def get(type):
        max_string_length = 1000
        max_int_size = 100000

        # if type == 'error':
        #     return error(identifier_list)
        if type.get_name() == 'bool':
            return randomizer.choice(["true", "false"])
        if type.get_name() == 'bit':
            return '"' + common.get_random_string(type.get_size(), False) + '"'
        if type.get_name() == 'varbit':
            return '"' + bin(common.get_random_number(0, type.get_size())) + '"'
        if type.get_name() == 'int':
            return common.get_random_number(0, type.get_size())
        return ''

