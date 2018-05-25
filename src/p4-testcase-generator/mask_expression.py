from expression import expression
from common import common


class mask_expression(object):
    type = 'mask_expression'
    left_expression = None
    right_expression = None

    def __init__(self, left_expression=None, right_expression=None):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def randomize(self):
        common.usedRandomize()
        self.left_expression = expression()
        self.left_expression.randomize()
        self.right_expression = expression()
        self.right_expression.randomize()

    def generate_code(self):
        return self.left_expression.generate_code() + ' &&& ' + self.right_expression.generate_code()



