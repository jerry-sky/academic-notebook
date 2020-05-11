
class LL_node(object):

    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class LList(object):
    """Simple linked list that is used as the chain inside HashTable.
    """

    def __init__(self):
        self._root = None
        self._find_comparisons = 0

    @property
    def find_comparisons(self):
        return self._find_comparisons

    def insert(self, new_value):
        if self._root is None:
            self._root = LL_node(new_value)
            return

        node = self._root
        while node.next is not None:
            node = node.next

        node.next = LL_node(new_value)

    def delete(self, value_to_delete):
        if self._root is None:
            return None
        elif self._root.value == value_to_delete:
            t = self._root
            self._root = None
            return t

        node = self._root.next
        previous = self._root
        while node is not None:
            if node.value == value_to_delete:
                previous.next = node.next
                return node
            previous = node
            node = node.next

        return None

    def find(self, search_value):
        if self._root is None:
            return None

        node = self._root
        while node is not None:
            self._find_comparisons += 1
            if node.value == search_value:
                return node
            node = node.next

        return None


