"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, function_to_apply, operator):
        self.function_to_apply = function_to_apply
        self.operator = operator

    def __call__(self, *args):
        return self.function_to_apply(*args)

    def __str__(self):
        return self.operator


if __name__ == '__main__':
    operator = DefaultOperator(lambda x, y: x + y, "+")
    assert operator.__call__(1, 2) == 3
    assert operator(1, 2) == 3
    assert operator.__str__() == "+"
    assert str(operator) == "+"
