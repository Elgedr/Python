"""."""

from abc import abstractmethod
from tree_node import TreeNode


class Operator(TreeNode):
    """Custom operation wrapper."""

    def __init__(self, *args):
        """Store the given arguments somehow."""
        super().__init__(*args)

    def apply(self):
        """Make use of the *args to compute the value of the given subtree. Recursion is your friend."""
        return self.default_operator(self._left.apply(), self._right.apply())

    def class_str(self):
        """:return class string representation of the object."""
        return f"{self.__class__.__name__}({self._left.class_str()},{self._right.class_str()})"

    def __str__(self):
        """:return the mathematical string representation of the tree with least amount of parenthesis."""
        operator_as_string = f" {self.default_operator.__str__()} "
        return f"{self._left.__str__()}{operator_as_string}{self._right.__str__()}"

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        our_operan = self.default_operator
        if our_operan == "+" or our_operan == "-" or our_operan == "&" or our_operan == "v" or our_operan == "xor":
            return True
        return False

    # @property
    # @abstractmethod
    # def default_operator(self):
    #     """abstract method which should be overridden to return the default_operator object."""
    #     pass

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Boolean whether the operation is associative or not.
        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def actions(self):
        """
        All custom implemented actions on different data structures.

        For example set - int does not exist, but we can implement it.
        :return a dictionary of functions where key is accepted parameters and value is a function which takes the
        aforementioned parameters as inputs and computes a value with them.
        """
        pass
