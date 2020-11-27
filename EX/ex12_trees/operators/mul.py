"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Mul(Operator):
    """Custom operation."""

    def __eq__(self, other):
        pass

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """priority of the operation."""
        return -1

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x * y, "*")

    @property
    def actions(self):
        """:return a dictionary of custom operations. Make use of frozensets."""
        return {
            (set, set): lambda x, y: {frozenset({itema, itemb}) for itema in x for itemb in y},  # cartesian product
            (set, int): lambda x, y: {frozenset({a, y}) for a in x},  # {1, 3} * 2 == {{1, 2}, {3, 2}}
            # (int, set): lambda x, y:  # 2 * {1, 3} == {{2, 1}, {2, 3}}
        }
