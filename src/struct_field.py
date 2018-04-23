import random
from common import common
from annotation import annotation
from base_type_generator import base_type_generator


class struct_field(object):
    name = ''
    annotation = None
    type = None

    common = common()
    base_type_generator = base_type_generator()

    min_field_name = 1
    max_field_name = 50

    def __init__(self, annotation=None, type=None, name=''):
        self.annotation = annotation
        self.type = type
        self.name = name

    def get_annotation(self):
        return self.annotation

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def generate_code(self):
        code = ''
        if self.annotation is not None:
            code += self.annotation.generate_code()
        code += ' ' + self.type.generate_code_ref()
        code += ' ' + self.name + ';'
        return code

    def randomize(self):
        _annotation = annotation()
        _annotation.randomize()
        self.annotation = _annotation
        self.type = self.base_type_generator.generate_random(['int', 'bit', 'varbit'])
        self.name = self.common.get_random_string(random.randint(self.min_field_name, self.max_field_name), False)