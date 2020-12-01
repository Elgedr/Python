"""."""

from tree_node import TreeNode
from default_operator import DefaultOperator


class Leaf(TreeNode):
    """Leaf node."""

    @property
    def default_operator(self):
        """Func."""
        return DefaultOperator(lambda x: x, "")

    def __init__(self, value):
        """default constructor."""
        super().__init__(value)
        self.__value = value

    def apply(self):
        """:return the value."""
        return self.__value

    def class_str(self):
        """:return class string representation of the object."""
        return f"Leaf({self.__value})"

    def __str__(self):
        """return string format of value."""
        return str(self.__value)

    def __eq__(self, other):
        """Equlizer."""
        if self.__value == other.apply() and self.class_str() == other.class_str():
            return True
        return False
