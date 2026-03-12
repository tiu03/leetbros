"""1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""

# Solution 1: Brute Force Approach -> O(n^2)

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    print("no such numbers exist in the array that sum to target")
    return None


# answer = twoSum(nums, target)
# print(answer)

"""
    TypeError: cannot unpack non-iterable int object
        - Cant use "for i,j in nums" because it outputs values of elements not their indices.
        - i++ not needed in for-in loop as its a for-each loop by default, which iterates through each element.
        - range() function params are (start, stop, step) where start is inclusive and stop is exclusive,
"""


# Solution 2: Using Hash Map
def twoSumHash(nums, target):
    myDict = {}

    for i in range(len(nums)):
        myDict[nums[i]] = i

    for i in range(len(nums)):
        ideal_j = target - nums[i]
        if ideal_j in myDict and myDict[ideal_j] != i:
            return [i, myDict[ideal_j]]


"""2. Given 2 linked lists l1 and l2, return the sum of the two lists as a linked list."""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    # Add one node at a time
    # Handle Carry: Add to next node, if at end Create new node
    # Handle Asymmetric lists
    l3 = ListNode()
    head = l3
    carry = 0
    sum = 0

    while l1 or l2 or carry:
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        l3.next = ListNode(sum % 10)
        l3 = l3.next
        carry = sum // 10  # reset carry by floor division
        sum = carry

    return head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
addTwoNumbers(l1, l2)
