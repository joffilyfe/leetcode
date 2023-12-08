from typing import Optional
import unittest


class Node:
    """Defines a Tree's node"""

    def __init__(
        self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node<{self.value}>"


def traverse(node: Node):
    """Access Tree's nodes from left to right, printing them."""
    if not node:
        return None

    print(node)

    if node.left:
        traverse(node.left)

    if node.right:
        traverse(node.right)


def find_depth(node: Optional[Node]):
    if not node:
        return -1

    return 1 + max(find_depth(node.left), find_depth(node.right))


def find_last_node(root: Optional[Node], value: int):
    """Traverse the Tree in order to find the last accesible node"""
    prev, current = None, root

    while current:
        prev = current

        if value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
        else:
            return current

    return prev


def find_node(root: Optional[Node], value: int):
    current = root

    while current:
        if not current:
            return None

        if value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
        elif value == current.value:
            return current


def insert_using_find(root: Node, value: int) -> Optional[Node]:
    if not root:
        return None

    current = find_last_node(root, value)

    if value < current.value:
        current.left = Node(value=value)
    elif value > current.value:
        current.right = Node(value=value)
    else:
        pass

    return root


def insert(root: Node, value: int):
    if not root:
        return Node(value=value)

    current = root

    while current:
        if value < current.value:
            if current.left:
                current = current.left
            else:
                current.left = Node(value=value)
                break
        elif value > current.value:
            if current.right:
                current = current.right
            else:
                current.right = Node(value=value)
                break
        else:
            break

    return root

def insert_recursive(root: Optional[Node], value: int) -> Node:
    if not root:
        return Node(value=value)

    if value < root.value:
        root.left = insert_recursive(root.left, value)
    elif value > root.value:
        root.right = insert_recursive(root.right, value)

    return root

def remove(root: Optional[Node], value: int) -> Optional[Node]:
    """Uses recursion to traverse the Three then removes target Node.

    It uses recursion to find out where is the most right->left Node
    in order to replace the target Node.
    """

    if not root:
        return None

    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if not root.right:
            root = root.left
            return root
        elif not root.left:
            root = root.right
            return root

        # branch at right side
        node = root.right

        # find the min at the right
        while node and node.left:
            node = node.left

        # switch the targer value by the min right->left found
        if node:
            root.value = node.value

        root.right = remove(root.right, root.value)

    return root


class TreeTest(unittest.TestCase):
    def setUp(self):
        self.root = Node(value=100)

    def test_creates_root_node(self):
        root = Node(value=0)

        self.assertEqual(root.value, 0)

    def test_inserts_left(self):
        insert(self.root, value=1)

        self.assertEqual(self.root.left.value, 1)
        self.assertIsNone(self.root.right)

    def test_inserts_right(self):
        insert(self.root, value=101)

        self.assertEqual(self.root.right.value, 101)
        self.assertIsNone(self.root.left)

    def test_removes_with_no_leaf(self):
        root = remove(self.root, 100)

        self.assertIsNone(root)

    def test_removes_with_no_left_in_right(self):
        #          100
        #         /   \
        #        10    101
        #       /  \  /   \
        #      N   N N     N

        # After removing 101
        #          100
        #         /   \
        #        10    N
        #       /  \
        #      N   N
        insert(self.root, 101)
        insert(self.root, 10)
        self.assertEqual(self.root.left.value, 10)

        remove(self.root, 101)
        self.assertEqual(self.root.left.value, 10)
        self.assertIsNone(self.root.right)


    def test_removes_with_two_leafs(self):
        #          100
        #         /   \
        #        10    null
        #       /  \
        #      9   12
        #     / \  /  \
        #    null 11 13

        # After removing
        #          100
        #         /   \
        #        11    null
        #       /  \
        #      9   12
        #     / \  /  \
        #    null null 13

        insert(self.root, 10)
        insert(self.root, 9)
        insert(self.root, 12)
        insert(self.root, 13)
        insert(self.root, 11)
        self.assertEqual(self.root.left.value, 10)

        remove(self.root, 10)
        self.assertEqual(self.root.left.value, 11)


unittest.main()
