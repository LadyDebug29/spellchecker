import damerau_levenshtein
from collections import defaultdict
from typing import Any, List


class BKTree:
    def __init__(self):
        self.tree: List[Any] = [None] * 1532630
        self._ptr = 0
        self.max_number_differences = 3

    def build_tree(self, parent_node, child_node):
        if self.tree[0] is None:
            self.tree[0] = parent_node

        dist = damerau_levenshtein.calculate_distance(parent_node.val, child_node.val)
        if parent_node.children[dist] == 0:
            self._ptr += 1
            self.tree[self._ptr] = child_node
            self.tree[self.tree.index(parent_node)].children[dist] = self._ptr
        else:
            self.build_tree(self.tree[parent_node.children[dist]], child_node)


class Node:
    def __init__(self, val=""):
        self.val = val
        self.children = defaultdict(int)
