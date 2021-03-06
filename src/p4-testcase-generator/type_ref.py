from base_type import base_type
from type_name import type_name
from specialized_type import specialized_type
from header_stack_type import header_stack_type
from randomizer import randomizer
from common import common


class type_ref(object):
    type = None
    types = ["baseType", "typeName", "specializedType", "headerStackType"]
    probabilities = [50,50,0,0]

    maxDepth = 5
    curDepth = 0

    force_type = None

    value = None

    # typeRef
    # : baseType
    # | typeName
    # | specializedType
    # | headerStackType
    # ;

    def __init__(self, value=None, force_type=None):
        self.value = value
        self.force_type = force_type

    def get_type(self):
        return self.types[self.type]

    def get_ref_type(self):
        return self.value.get_ref_type()

    def get_type_decl(self):
        return self.value.get_type_decl()

    def randomize(self):
        self.__class__.curDepth += 1
        while True:
            self.type = randomizer.getRandom(self.probabilities)
            if self.force_type is not None:
                self.type = self.force_type
            if self.type == 0:
                self.value = base_type()
            elif self.type == 1:
                self.value = type_name()
            elif self.type == 2:
                self.value = specialized_type()
            elif self.type == 3:
                self.value = header_stack_type()
            if self.__class__.curDepth < self.__class__.maxDepth:
                self.value.randomize()
                if not self.filter():
                    break
            else:
                self.__class__.curDepth -= 1
        self.__class__.curDepth -= 1

    def filter(self):
        if self.get_type() == "typeName":
            if self.value.prefixed_type is None:
                return True
        if self.get_type() == "specializedType":
            if self.value.prefixed_type is None:
                return True
        elif self.get_type() == "headerStackType":
            if self.value.type_name is None:
                return True
        return False

    def generate_code(self):
        common.usedCodeGenerator(self)
        return self.value.generate_code()
