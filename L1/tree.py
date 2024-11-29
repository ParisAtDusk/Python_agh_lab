import unittest

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node, edge_value=None):
        self.children.append(TreeEdge(node, edge_value))

    def __str__(self):
        return str(self.value)


class TreeEdge:
    def __init__(self, node, value=None):
        self.node = node
        self.value = value

    def __str__(self):
        return f"{self.value}" if self.value is not None else "No edge label"


class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value)

    def traverse(self):
        result = []
        self._traverse_recursive(self.root, result)
        return result

    def _traverse_recursive(self, node, result):
        result.append(node.value)
        for edge in node.children:
            self._traverse_recursive(edge.node, result)

    def __str__(self):
        return self._str_recursive(self.root, level=0)

    def _str_recursive(self, node, level):
        result = "  " * level + f"Node({node.value})\n"
        for edge in node.children:
            result += "  " * (level + 1) + f"Edge({edge}) -> "
            result += self._str_recursive(edge.node, level + 2)
        return result


# Example of creating a tree
tree = Tree("root")
child1 = TreeNode("child1")
child2 = TreeNode("child2")

tree.root.add_child(child1, edge_value="edge1")
tree.root.add_child(child2, edge_value="edge2")

# Adding grandchildren
child1.add_child(TreeNode("grandchild1"))
child2.add_child(TreeNode("grandchild2"))

# Print the tree structure
print(tree)
# Output the traversal
print("Traversal:", tree.traverse())


class TestTree(unittest.TestCase):
    def setUp(self):
        # Setup a sample tree for testing
        self.tree = Tree("root")
        self.child1 = TreeNode("child1")
        self.child2 = TreeNode("child2")

        # Adding children to the root
        self.tree.root.add_child(self.child1, edge_value="edge1")
        self.tree.root.add_child(self.child2, edge_value="edge2")

        # Adding grandchildren
        self.child1.add_child(TreeNode("grandchild1"))
        self.child2.add_child(TreeNode("grandchild2"))

    def test_traverse(self):
        expected_traversal = ["root", "child1", "grandchild1", "child2", "grandchild2"]
        self.assertEqual(self.tree.traverse(), expected_traversal)

    def test_str(self):
        tree_str = str(self.tree)
        # Check that basic node structure appears in the string representation
        self.assertIn("Node(root)", tree_str)
        self.assertIn("Edge(edge1) ->   Node(child1)", tree_str)
        self.assertIn("Node(grandchild2)", tree_str)

    def test_edge_values(self):
        # Check if edge values are correctly set
        self.assertEqual(self.tree.root.children[0].value, "edge1")
        self.assertEqual(self.tree.root.children[1].value, "edge2")


unittest.main()


