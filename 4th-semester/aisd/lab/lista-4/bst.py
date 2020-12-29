from typing import List


class BST_node(object):
    """Atomic structure used inside binary search trees.
    """

    def __init__(self, value: str, left=None, right=None, parent=None):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new_left):
        self._left = new_left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, new_right):
        self._right = new_right

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent


class BST(object):
    """Data structure that stores values in very naive and simple binary
    trees that don't self balance.
    """

    def __init__(self):
        self._root = None
        self._nodes_count = 0
        self._find_comparisons = 0

    @property
    def nodes_count(self):
        return self._nodes_count

    @property
    def find_comparisons(self):
        return self._find_comparisons

    def _node_insert(self, new_node: BST_node) -> BST_node:
        """Inserts the node into the tree.

        This method is separated from the `insert` method to ensure futher
        expandability, e.g. RB-Trees.
        """
        parent = None
        node = self._root
        while node is not None:
            parent = node
            if new_node.value < node.value:
                node = node.left
            else:  # new_node.value >= node.value
                node = node.right
        # new_node = BST_node(new_value, parent=parent)
        new_node.parent = parent
        if parent is None:
            self._root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:  # new_value >= parent.value
            parent.right = new_node

        self._nodes_count += 1
        return new_node

    def insert(self, new_value: str) -> BST_node:
        """Inserts a new value into the tree.
        """
        new_node = BST_node(new_value)
        return self._node_insert(new_node)

    def find(self, value_to_find: str) -> BST_node:
        """Finds the node that contains provided search value.
        Returns `None` if value not found
        """
        node = self._root

        while node is not None:
            self._find_comparisons += 1
            if node.value == value_to_find:
                return node
            if value_to_find < node.value:
                node = node.left
            else:  # value_to_find >= node.value
                node = node.right

        return None

    @staticmethod
    def node_minimum(node: BST_node) -> BST_node:
        """Returns the node that contains the minimum value in the subtree
        of the provided `node`.
        """
        if node is None:
            return None
        t = node
        while t.left is not None:
            t = t.left
        return t

    def minimum(self) -> BST_node:
        """Returns the node that contains the minimum value in the BST.
        """
        return BST.node_minimum(self._root)

    @staticmethod
    def node_maximum(node: BST_node) -> BST_node:
        """Returns the node that contains the maximum value in the subtree
        of the provided `node`.
        """
        if node is None:
            return None
        t = node
        while t.right is not None:
            t = t.right
        return t

    def maximum(self) -> BST_node:
        """Returns the node that contains the maximum value in the BST.
        """
        return BST.node_maximum(self._root)

    def successor(self, value_to_succ: str) -> BST_node:
        node = self.find(value_to_succ)
        if node is None:
            return None
        if node.right is not None:
            return BST.node_minimum(node.right)

        parent = node.parent

        while parent is not None and node is parent.right:
            node = parent
            parent = parent.parent

        return parent

    def delete(self, value_to_delete: str) -> BST_node:
        """Deletes the node that contains provided value.
        """
        parent = None
        node = None
        node_to_delete = self.find(value_to_delete)
        if node_to_delete is None:
            return None

        if node_to_delete.left is None or node_to_delete.right is None:
            parent = node_to_delete
        else:
            parent = self.successor(value_to_delete)

        if parent.left is not None:
            node = parent.left
        else:
            node = parent.right

        if node is not None:
            node.parent = parent.parent

        if parent.parent is None:
            self._root = node
        elif parent is parent.parent.left:
            parent.parent.left = node
        else:
            parent.parent.right = node

        if parent is not node_to_delete:
            node_to_delete.value = parent.value
            node_to_delete.parent = parent.parent
            node_to_delete.left = parent.left
            node_to_delete.right = parent.right

        self._nodes_count -= 1
        return parent

    @staticmethod
    def node_inorder(node: BST_node) -> List[str]:
        """Returns elements of the `node` subtree in sorted order.
        """
        if node is not None:
            return BST.node_inorder(node.left) + [node.value] + BST.node_inorder(node.right)
        else:
            return []

    def inorder(self) -> List[str]:
        """Returns elements of the BST in sorted order.
        """
        return BST.node_inorder(self._root)

