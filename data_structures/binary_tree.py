class BinaryTree:

    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def put(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self._put(self.root, value)
        self.size += 1

    def _put(self, current_node, value):
        if current_node.value < value:
            if current_node.has_left_child():
                self._put(current_node.left_child, value)
            else:
                current_node.left_child = BinaryTreeNode(value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(current_node.right_child, value)
            else:
                current_node.right_child = BinaryTreeNode(value, parent=current_node)


class BinaryTreeNode:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_child = right

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


if __name__ == '__main__':
    tree = BinaryTree()
    tree.put(10)
    tree.put(20)
    tree.put(2)
