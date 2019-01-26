"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:

    @staticmethod
    def bruteforce_solution(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v_i in enumerate(nums):
            for j, v_j in enumerate(nums):
                if i != j and v_i + v_j == target:
                    return [i, j]
        return []

    @staticmethod
    def two_way_hashmap_solution(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values_map = {value: idx for idx, value in enumerate(nums)}

        for first_value in nums:
            second_value = target - first_value
            if second_value in values_map.keys() and values_map[first_value] != values_map[second_value]:
                return [values_map[first_value], values_map[second_value]]
        return []

    @staticmethod
    def one_way_hashmap_solution(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values_map = {}

        for idx, first_value in enumerate(nums):
            second_value = target - first_value
            if second_value in values_map.keys():
                return [idx, values_map[second_value]]
            values_map[first_value] = idx
        return []


if __name__ == '__main__':

    solution = Solution()

    target = 9
    nums = [2, 7, 11, 15]

    print('Full bruteforce solution: ', solution.bruteforce_solution(nums, target))
    print('Two-way hashmap solution: ', solution.bruteforce_solution(nums, target))
    print('One-way hashmap solution: ', solution.bruteforce_solution(nums, target))
