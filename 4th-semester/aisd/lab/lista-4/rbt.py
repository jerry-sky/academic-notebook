from typing import List
from enum import Enum
from bst import BST_node, BST


class RBT_colour(Enum):
    red = 'red'
    black = 'black'


class RBT_node(BST_node):

    def __init__(self, value: str, left=None, right=None, parent=None, colour=RBT_colour.black):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent
        self._colour = colour

    @classmethod
    def from_BST_node(bst_node: BST_node):
        rbt_node = RBT_node(
            bst_node.value, left=bst_node.left,
            right=bst_node.right, parent=bst_node.parent)
        return rbt_node

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, new_colour: RBT_colour):
        self._colour = new_colour


class RBT(BST):
    """Augmented BST data structure that does self balance.
    """

    def left_rotate(self, x: RBT_node):
        """Rotates to the left some nodes pivoting round the `x` node.
        """
        y = x.right  # y is the node that will be lifted up
        x.right = y.left  # subtree B „owned” by x

        if y.left is not None:
            y.left.parent = x  # fix the parent of the root of the B subtree

        y.parent = x.parent  # former parent of x shall be the new parent of y

        if x.parent is None:
            self._root = y  # y is the new root of the whole tree
        elif x is x.parent.left:  # y goes under x's parent
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x: RBT_node):
        """Rotates to the right some nodes pivoting round the `x` node.
        """
        y = x.left
        x.left = y.right

        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self._root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def insert(self, new_value: str) -> None:
        """Inserts a new value into the tree.
        """
        x = self._node_insert(
            RBT_node(new_value, colour=RBT_colour.red))

        while x is not self._root and x.parent.colour == RBT_colour.red:
            if x.parent.parent is None:
                return
            if x.parent is x.parent.parent.left:
                y = x.parent.parent.right
                if y is not None and y.colour == RBT_colour.red:  # case #1
                    x.parent.colour = RBT_colour.black
                    y.colour = RBT_colour.black
                    x.parent.parent.colour = RBT_colour.red
                    x = x.parent.parent
                else:
                    if x is x.parent.right:  # case #2
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.colour = RBT_colour.black  # case #3
                    x.parent.parent.colour = RBT_colour.red
                    self.right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y is not None and y.colour == RBT_colour.red:  # case #1
                    x.parent.colour = RBT_colour.black
                    y.colour = RBT_colour.black
                    x.parent.parent.colour = RBT_colour.red
                    x = x.parent.parent
                else:
                    if x is x.parent.left:  # case #2
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.colour = RBT_colour.black  # case #3
                    x.parent.parent.colour = RBT_colour.red
                    self.left_rotate(x.parent.parent)
            self._root.colour = RBT_colour.black

    def _delete_fixup(self, x: RBT_node):
        while x is not None and x is not self._root and x.colour == RBT_colour.black:
            if x is x.parent.left:
                w = x.parent.right
                if w.colour == RBT_colour.red:
                    w.colour = RBT_colour.black
                    x.parent.colour = RBT_colour.red
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.colour == RBT_colour.black and w.right.colour == RBT_colour.black:
                    w.colour = RBT_colour.red
                    x = x.parent
                else:
                    if w.right.colour == RBT_colour.black:
                        w.left.colour = RBT_colour.black
                        w.colour = RBT_colour.red
                        self.right_rotate(w)
                        w = x.parent.right
                    w.colour = x.parent.colour
                    x.parent.colour = RBT_colour.black
                    w.right.colour = RBT_colour.black
                    self.left_rotate(x.parent)
                    x = self._root
            else:
                w = x.parent.left
                if w.colour == RBT_colour.red:
                    w.colour = RBT_colour.black
                    x.parent.colour = RBT_colour.red
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.colour == RBT_colour.black and w.right.colour == RBT_colour.black:
                    w.colour = RBT_colour.red
                    x = x.parent
                else:
                    if w.left.colour == RBT_colour.black:
                        w.right.colour = RBT_colour.black
                        w.colour = RBT_colour.red
                        self.left_rotate(w)
                        w = x.parent.left
                    w.colour = x.parent.colour
                    x.parent.colour = RBT_colour.black
                    w.left.colour = RBT_colour.black
                    self.right_rotate(x.parent)
                    x = self._root
        if x is not None:
            x.colour = RBT_colour.black


    def delete(self, value_to_delete):
        z = self.find(value_to_delete)
        if z is None:
            return None

        y = None
        x = None
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.successor(z.value)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self._root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y is not z:
            z.value = y.value
            z.parent = y.parent
            z.left = y.left
            z.right = y.right
            z.colour = y.colour

        if y.colour == RBT_colour.black:
            self._delete_fixup(x)

        self._nodes_count -= 1
        return y

