import random
from base_type import base_type
from type_name import type_name
from specialized_type import specialized_type
from header_stack_type import header_stack_type
from common import common
from randomizer import randomizer


class type_ref(object):
    type = None
    types = ["baseType", "typeName", "specializedType", "headerStackType"]
    probabilities = [2,3,2,3]

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

    def get_type(self):
        return self.types[self.type]

    def randomize(self):
        self.__class__.curDepth += 1
        while True:
            self.type = randomizer.getRandom(self.probabilities)
            if self.type == 0:
                self.value = base_type()
            elif self.type == 1:
                self.value = type_name()
            elif self.type == 2:
                self.value = specialized_type()
            elif self.type == 3:
                self.value = header_stack_type()
            self.value.randomize()
            if not self.filter():
                break
        self.__class__.curDepth -= 1

    def filter(self):
        if self.__class__.curDepth > self.__class__.maxDepth:
            return True
        elif self.get_type() == "typeName" or self.get_type() == "specializedType":
            if self.value.prefixed_type is None:
                return True
        elif self.get_type() == "headerStackType":
            if self.value.type_name is None:
                return True
        return False

    def generate_code(self):
        return self.value.generate_code()
