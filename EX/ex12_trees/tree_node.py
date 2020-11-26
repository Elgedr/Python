"""."""

from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    """The main node class."""

    def __init__(self, *args):
        """:param make use of *args and store them in a way that it is easy to use them."""
        # self.__value = args  # tuple of values
        element = args[0]
        if type(element) == tuple:
            self._left = element[0]
            self._right = element[1]
        else:
            self._value = element

    # @property
    # @abstractmethod
    # def default_operator(self):
    #     """a."""
    #     return lambda *x: x

    @abstractmethod
    def apply(self):
        """abstract method which should be overridden to compute the value of the given abstract tree."""
        pass

    @abstractmethod
    def class_str(self):
        """:return class string representation of the object."""
        pass

    @abstractmethod
    def __str__(self):
        """:return string representation of the object."""
        pass

    def __eq__(self, other):
        """:return True when 2 object trees have the same shape and values."""
        if self is other:
            return True
        return False

    def __ne__(self, other):
        """:return True when 2 object trees have a different shape and/or values."""
        if self is not other:
            return True
        return False