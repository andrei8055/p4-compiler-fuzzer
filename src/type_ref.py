import random
from base_type import base_type
from type_name import type_name
from specialized_type import specialized_type
from header_stack_type import header_stack_type
from common import common

class type_ref(object):
    type = 'type_ref'

    maxDepth = 1
    curDepth = 0

    value = None

    # typeRef
    # : baseType
    # | typeName
    # | specializedType
    # | headerStackType
    # ;

    def __init__(self, value=None):
        self.value = value

    def randomize(self):
        common.usedRandomize()
        self.__class__.curDepth += 1
        rnd = random.randint(0, 3)
        if self.__class__.curDepth > self.__class__.maxDepth:
            # TODO: probability table update to avoid rule 2
            rnd = 0
        if rnd == 0:
            self.value = base_type()
        elif rnd == 1:
            self.value = type_name()
        elif rnd == 2:
            self.value = specialized_type()
        elif rnd == 3:
            self.value = header_stack_type()
        self.value.randomize()
        self.__class__.curDepth -= 1

    def generate_code(self):
        return self.value.generate_code()
