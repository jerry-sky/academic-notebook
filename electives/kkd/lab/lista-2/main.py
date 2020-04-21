#!/usr/bin/python3
from functools import reduce
from sys import argv, exit
from typing import List
import math

# the „Not Yet Transmitted”
NYT_CHAR_CODE = 'NYT'


class Node(object):

    def __init__(self, parent, weight=0, left=None, right=None, char=''):
        self._parent = parent
        self._weight = weight
        self._left = left
        self._right = right
        self._char = char

    @property
    def parent(self): return self._parent
    @parent.setter
    def parent(self, new_parent): self._parent = new_parent

    @property
    def weight(self): return self._weight
    @weight.setter
    def weight(self, new_weight): self._weight = new_weight

    @property
    def left(self): return self._left
    @left.setter
    def left(self, new_left): self._left = new_left

    @property
    def right(self): return self._right
    @right.setter
    def right(self, new_right): self._right = new_right

    @property
    def char(self): return self._char
    @char.setter
    def char(self, new_char): self._char = new_char

    def is_leaf(self):
        """A node is a leaf when it doesn't have any children.
        """
        return self._left is None and self._right is None


class HuffmanCoding(object):
    """Encodes and decodes a Huffman code written in binary.
    """

    def __init__(self):
        self._NYT = Node(None, 0, char=NYT_CHAR_CODE)
        self._root = self._NYT
        # initialize a master list of all characters that have appeared
        # prepare it so it can hold references to 256 ASCII characters
        # each node is mapped to the id of ASCII character it's holding
        self._all_chars: List[Node] = [None] * 256
        self._all_nodes_sorted: List[Node] = []

    def _is_already_added(self, char: str):
        """Check if the character has already been added.
        """
        if ord(char) > 255:
            raise Exception('character out of range... somehow')

        if self._all_chars[ord(char)] is not None:
            return True
        return False

    def _register_char(self, char: str):
        """Inserts a new character or increases weight of an already added one.
        """
        curr = self._all_chars[ord(char)]

        if curr is None:
            # first time for this character
            nyt = self._NYT
            old_nyt_parent = nyt.parent

            new_parent = None

            if old_nyt_parent is None:
                # special case - inserting the first character, NYT is the root node
                self._root = Node(None, left=nyt, right=None)
                nyt.parent = self._root
                new_parent = self._root
            else:
                # create a new intermediatary node
                new_parent = Node(old_nyt_parent, weight=1,
                                  left=nyt, right=None)
                # rewire the nodes
                old_nyt_parent.left = new_parent
                nyt.parent = new_parent

            # wire up the new node to the new parent
            new_node = Node(new_parent, weight=1, char=char)
            new_parent.right = new_node

            # save these newly generated nodes into the master nodes list
            self._all_nodes_sorted.append(new_node)
            self._all_nodes_sorted.append(new_parent)

            # save this new node into the master char list
            self._all_chars[ord(char)] = new_node

            curr = new_parent.parent

        # now when we've made sure the node exists we need to increase weight
        while curr is not None:

            # find the first node that has the same weight as this
            # because this `curr` node will have its weight increased
            # so it will be +1 more than the node we're searching for now:
            to_swap = None
            for n in self._all_nodes_sorted:
                if n.weight == curr.weight:
                    # found one
                    to_swap = n
                    break

            if curr is not to_swap and curr is not to_swap.parent and to_swap is not curr.parent:
                self._swap_nodes(curr, to_swap)

            curr.weight += 1
            curr = curr.parent

    def _swap_nodes(self, one: Node, two: Node):
        """Swap two provided nodes with each other.
        """
        one_index = self._all_nodes_sorted.index(one)
        two_index = self._all_nodes_sorted.index(two)

        # swap the nodes in the master nodes list
        self._all_nodes_sorted[one_index], self._all_nodes_sorted[
            two_index] = self._all_nodes_sorted[two_index], self._all_nodes_sorted[one_index]

        parent = one.parent
        one.parent = two.parent
        two.parent = parent

        # make sure everything is wired up correctly
        if one.parent.left is two:
            one.parent.left = one
        else:
            one.parent.right = one

        if two.parent.left is one:
            two.parent.left = two
        else:
            two.parent.right = two

    def _get_node_code(self, _node: Node):
        """Generates binary path from the root node to the provided node.
        """
        code = ''
        node = _node
        while node.parent is not None:
            p = node.parent
            if p.left is node:
                code += '0'
            else:  # p.right is node
                code += '1'
            node = p
        # invert the code because decoder will start at the root node,
        # not at the node that is trying to decode
        return code[::-1]

    def _get_code(self, char: str):
        """Generates current Huffman code for the provided character.
        """
        if self._is_already_added(char):
            # reconstruct the code
            node = self._all_chars[ord(char)]
            return self._get_node_code(node)
        else:
            # the character hasn't appeared before so we need to send
            # code for NYT first and then the ASCII code of that character
            # NYT code + character's ASCII code
            return self._get_node_code(self._NYT) + bin(ord(char))[2:].zfill(8)

    def encode_single_character(self, char: str) -> str:
        """Adds the character to the coding tree and returns current
        Huffman code for the character.
        """
        code = self._get_code(char)
        self._register_char(char)
        return code

    def decode(self, encoded: str) -> List[int]:
        """Decode Huffman-encoded file.
        """

        output = []

        # read the first character which will be just ASCII coded character
        first_char = chr(int(encoded[:8], 2))

        output.append(ord(first_char))

        self._register_char(first_char)

        node = self._root
        # already decoded first 8 bits
        i = 8
        while i < len(encoded):
            # current bit
            curr = encoded[i]

            if curr == '0':
                node = node.left
            elif curr == '1':
                node = node.right
            else:
                raise Exception("invalid Huffman code (not a 0 or 1)")

            char = node.char

            if char:
                if char == NYT_CHAR_CODE:
                    char = chr(int(encoded[i+1:i+9], 2))
                    i += 8
                output.append(ord(char))
                self._register_char(char)
                node = self._root

            i += 1

        return output

    def get_avg_code_length(self):
        """Calculates average codeword length.
        """

        lengths = []
        count = 0

        for char in self._all_chars:
            if char is None:
                continue
            lengths.append(len(self._get_node_code(char)))
            count += 1

        return sum(lengths) / count

    def get_entropy(self):
        """Calculates the entropy.
        """
        output = 0

        for char in self._all_chars:
            if char is None:
                continue
            output += char.weight * (-math.log2(char.weight))

        output /= self._root.weight

        return output + math.log2(self._root.weight)


if __name__ == "__main__":

    # parse the arguments
    args = argv[1:]

    if len(args) < 3:
        exit("usage: ./main.py <--encode|--decode> <input file> <output file>")

    mode = args[0]
    input_file = args[1]
    output_file = args[2]

    huffman = HuffmanCoding()

    if mode == "--decode":
        with open(output_file, "wb+") as fo:
            with open(input_file, "rb") as fi:
                input_bits = ""
                tmp = fi.read(1)
                # first byte is an indicator to say how much padding bits
                # were used to fill the last byte
                padding_used = ord(tmp)

                tmp = fi.read(1)
                while tmp:
                    tmp = ord(tmp)
                    for i in range(0, 8):
                        if (tmp >> (7-i)) & 0b1:
                            input_bits += '1'
                        else:
                            input_bits += '0'
                    tmp = fi.read(1)

                # trim the padding
                input_bits = input_bits[:-padding_used]

                bytes_ = huffman.decode(input_bits)
                for b in bytes_:
                    fo.write(b.to_bytes(1, byteorder="big"))

    else:  # mode == --encode
        with open(output_file, "wb+") as fo:
            with open(input_file, "rb") as fi:
                output = ""
                byte = fi.read(1)
                count = 1
                while byte:
                    output += huffman.encode_single_character(byte)
                    byte = fi.read(1)
                    count += 1

                # convert to actual bytes
                output_bytes = []
                padding_used = 0
                for i in range(0, math.ceil(len(output)/8)):
                    tmp = output[(i*8):((i+1)*8)]
                    if len(tmp) != 8:
                        # last remaining batch of bits needs to be padded
                        # to fit into a full-sized byte
                        padding_used = 8-len(tmp)
                        tmp += "0" * padding_used
                    tmp = int(tmp, 2)
                    output_bytes.append(tmp)
                # first byte indicates how much padding was used
                output_bytes = [padding_used] + output_bytes

                # write output bytes
                for b in output_bytes:
                    fo.write(b.to_bytes(1, byteorder='big'))

                # print stats
                print("avg codeword length:", huffman.get_avg_code_length())
                print("compression rate:", count/len(output_bytes))
                print("entropy:", huffman.get_entropy())
