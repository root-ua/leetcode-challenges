"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next


class Solution:

    def get_list(self, l, out=None):
        if l is None:
            return out

        if out is None and l.next is None:
            return [str(l.val)]
        elif out is None:
            return self.get_list(l.next, out=[str(l.val)])
        else:
            out.append(str(l.val))
            return self.get_list(l.next, out=out)

    def get_input(self, l):
        return int(''.join(list(reversed(self.get_list(l)))))

    def addTwoNumbers(self, l1, l2):

        n1 = self.get_input(l1)
        n2 = self.get_input(l2)
        results = list(reversed((str(n1 + n2))))

        root_node, previous_node = None, None

        for digit in results:
            list_node = ListNode(digit)
            if root_node is None:
                root_node = list_node
            if previous_node:
                previous_node.next = list_node
            previous_node = list_node

        return root_node


if __name__ == '__main__':

    solution = Solution()

    l1 = ListNode(2, _next=ListNode(4, _next=ListNode(3)))
    l2 = ListNode(5, _next=ListNode(6, _next=ListNode(4)))
    result_1 = solution.addTwoNumbers(l1, l2)

    print(
        'Input: ', solution.get_input(l1), '; ', solution.get_input(l2),
        'Output: ', solution.get_input(result_1)
    )

    l3 = ListNode(1, _next=ListNode(8))
    l4 = ListNode(0)
    result_2 = solution.addTwoNumbers(l3, l4)

    z = 1

    print(
        'Input: ', solution.get_input(l3), '; ', solution.get_input(l4),
        'Output: ', solution.get_input(result_2)
    )
