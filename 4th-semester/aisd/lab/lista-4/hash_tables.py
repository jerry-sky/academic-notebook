from llist import LList
from rbt import RBT

# $n_t$ - more about this variable in ./readme.md
HASH_TABLE_RBT_SWITCH_THRESHOLD = 40

def default_hashing_func(x: str) -> int:
    output = 11
    for char in x:
        output = output * 41 + ord(char)
    return output


class HashTable(object):
    """Hash table that uses chain rule. Switches to RB-Trees when large
    quantity of data is being inserted into the same hash address.
    """

    def __init__(self, size: int, hashing_func=default_hashing_func):
        self._data = [LList() for _ in range(0, size)]
        self._data_length = [0 for _ in range(0, size)]
        self._size = size
        self._hashing_func = hashing_func

        self._nodes_count = 0

    @property
    def nodes_count(self):
        return self._nodes_count

    def _get_index(self, value) -> int:
        return self._hashing_func(value) % self._size

    def insert(self, new_value: str) -> None:
        """Inserts a new value to the hash table.
        """
        index = self._get_index(new_value)
        # switch to RB-Tree when it seems necessary
        if self._data_length[index] == HASH_TABLE_RBT_SWITCH_THRESHOLD:
            # create a new RB-Tree and move all the values to it
            # from the original linked list
            rbt = RBT()
            node = self._data[index]._root
            while node is not None:
                rbt.insert(node.value)
                node = node.next
            self._data[index] = rbt
            # to avoid unnecessary switching to RB-Tree when it has already been done
            # make the data length basically unchangable
            # float('inf') + 123 = float('inf')
            self._data_length[index] = float('inf')

        self._data[index].insert(new_value)
        self._data_length[index] += 1

        self._nodes_count += 1


    def find(self, search_value: str) -> str:
        """Returns a truthy value when the provided value is present
        in the hash table.
        """
        node = self._data[self._get_index(search_value)].find(search_value)
        if node is not None:
            return node.value

    def delete(self, value_to_delete: str) -> None:
        """Removes the provided value from the hash table.
        """
        self._data[self._get_index(value_to_delete)].delete(value_to_delete)
        self._data_length[self._get_index(value_to_delete)] -= 1

        self._nodes_count -= 1
