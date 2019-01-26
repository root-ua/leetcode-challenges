class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


def traverse(node):
    """
    Traversing a Linked List
    :param node: Linked List node to start with.
    :return: List of values stored in a Linked List.
    """
    _output = []
    while node is not None:
        assert isinstance(node, LinkedListNode), 'Node should be a type of LinkedListNode.'
        _output.append(node.value)
        node = node.next
    return _output


def deduplicate(node):
    """
    Deduplicated orginal Linked List.
    :param node: Linked List node to start with.
    :return: New root / starting node of a deduplicated Linked List.
    """

    existing_values = []
    root_node, previous_node = None, None

    while node is not None:

        if root_node is None:
            root_node = LinkedListNode(node.value)
            previous_node = root_node
            existing_values.append(node.value)

        elif node.value not in existing_values:
            previous_node.next = LinkedListNode(node.value)
            previous_node = previous_node.next
            existing_values.append(node.value)

        node = node.next

    return root_node


if __name__ == '__main__':

    node1 = LinkedListNode(5)
    node2 = LinkedListNode(10)
    node3 = LinkedListNode(15)
    node4 = LinkedListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    output_traversed = traverse(node1)
    print('Traversed linked list: ', output_traversed)

    output_deduplicated = traverse(deduplicate(node1))
    print('Traversed deduplicated linked list: ', output_deduplicated)

