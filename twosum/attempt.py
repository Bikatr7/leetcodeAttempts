from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Create a dictionary to store the values and their indices
        dict = {}

        for index, num in enumerate(nums):

            ## Check if the difference between the target and the current number is in the dictionary
            if target - num in dict:
                return [dict[target - num], index]
            
            ## If the difference is not in the dictionary, add the current number and its index to the dictionary
            dict[num] = index
        