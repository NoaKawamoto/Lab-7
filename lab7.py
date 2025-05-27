from dataclasses import dataclass
import unittest


@dataclass
class BinaryTree:
    key: int
    left: "BinaryTree" = None
    right: "BinaryTree" = None


@dataclass
class BinaryTreeMerger:
    def merge(self, tree_1: BinaryTree, tree_2: BinaryTree) -> BinaryTree:
        if not tree_1 and not tree_2:
            return None
        elif not tree_1:
            return tree_2
        elif not tree_2:
            return tree_1

        merged = BinaryTree(tree_1.key + tree_2.key)
        merged.left = self.merge(tree_1.left, tree_2.left)
        merged.right = self.merge(tree_1.right, tree_2.right)
        return merged


def compare_trees(t1: BinaryTree, t2: BinaryTree) -> bool:
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (
            t1.key == t2.key
            and trees_are_equal(t1.left, t2.left)
            and trees_are_equal(t1.right, t2.right)
    )


class TestBinaryTreeMerger(unittest.TestCase):
    def setUp(self):
        self.merger = BinaryTreeMerger()

    def test_merge(self):
        tree_1 = BinaryTree(1)
        tree_1.left = BinaryTree(3)
        tree_1.right = BinaryTree(2)
        tree_1.left.left = BinaryTree(5)

        tree_2 = BinaryTree(2)
        tree_2.left = BinaryTree(1)
        tree_2.right = BinaryTree(3)
        tree_2.left.right = BinaryTree(4)
        tree_2.right.right = BinaryTree(7)

        expected = BinaryTree(3)
        expected.left = BinaryTree(4)
        expected.right = BinaryTree(5)
        expected.left.left = BinaryTree(5)
        expected.left.right = BinaryTree(4)
        expected.right.right = BinaryTree(7)

        result = self.merger.merge(tree_1, tree_2)
        self.assertTrue(trees_are_equal(result, expected))

    def test_skewed_left(self):
        tree_1 = BinaryTree(1, BinaryTree(2, BinaryTree(3)))
        tree_2 = BinaryTree(4, BinaryTree(5, BinaryTree(6)))

        expected = BinaryTree(5)
        expected.left = BinaryTree(7)
        expected.left.left = BinaryTree(9)

        result = self.merger.merge(tree_1, tree_2)
        self.assertTrue(trees_are_equal(result, expected))


def test_both_empty(self):
    tree_1 = None
    tree_2 = None
    result = self.merger.merge(tree_1, tree_2)
    self.assertIsNone(result)


def test_skewed_right(self):
    tree_1 = BinaryTree(1, None, BinaryTree(2, None, BinaryTree(3)))
    tree_2 = BinaryTree(4, None, BinaryTree(5, None, BinaryTree(6)))

    expected = BinaryTree(5)
    expected.right = BinaryTree(7)
    expected.right.right = BinaryTree(9)

    result = self.merger.merge(tree_1, tree_2)
    self.assertTrue(trees_are_equal(result, expected))


def test_one_empty(self):
    tree_1 = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    tree_2 = None

    expected = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    result = self.merger.merge(tree_1, tree_2)
    self.assertTrue(trees_are_equal(result, expected))


if __name__ == "__main__":
    unittest.main()

