class Node(object):
    """
    Node contains two objects - a left and a right child, both may be a Node or both None,
    latter representing a leaf
    """

    def __init__(self, left=None, right=None):
        super(Node, self).__init__()
        self.left = left
        self.right = right

    def __str__(self):
        """
        Default inorder print
        """
        if self.left is None and self.right is None:
            return "(   )"
        else:
            return "( " + str(self.left) + " " + str(self.right) + " )"

    def __eq__(self, other):
        if self.left is None and self.right is None:
            return other.left is None and other.right is None
        elif other.left is None and other.right is None:
            return False
        else:
            return self.left == other.left and self.right == other.right


def mirrorTree(node):
    """
    Returns the mirror image of the tree rooted at node
    """
    if node == Node():
        mirror_node = Node()
    else:
        mirror_node = Node(mirrorTree(node.right), mirrorTree(node.left))
    return mirror_node


def allTrees(n):
    """
    Returns a list of all unique trees with n internal nodes
    """
    trees = []
    return trees


def allSymTrees(n):
    """
    Returns a list of all unique symmetrical trees with n internal nodes
    """
    if n % 2:
        return [Node(sub_tree, sub_tree) for sub_tree in allTrees(n // 2)]
    else:
        return []


if __name__ == '__main__':
    # for x in allSymTrees(int(input())):
    #     print(x)
    node = Node(Node(Node(), Node(Node(), Node())), Node())
    print(node)
    print(mirrorTree(node))
