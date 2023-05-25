# Given an integer array, return true if any value appears at least twice in the array and return false if every element is distinct

class Solution:
    
    # Brute force solution --> Time complexity: O(n^2)
    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:
        count = 0
        
        while count < len(nums):
            number = nums[count]
            inner_counter = count + 1
            while inner_counter < len(nums):
                if nums[inner_counter] == number:
                    return True
                inner_counter += 1
            
            count += 1

        return False

    # Sorting solution --> Time complexity: O(nlogn)
    def contains_duplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        
        for number in range(len(nums)):
            if number != len(nums) - 1:
                if nums[number] == nums[number + 1]:
                    return True
        
        return False
    
    # Hashing solution --> Time complexity: O(n)
    def contains_duplicate_hashset(self, nums: List[int]) -> bool:
        hashset = set()
        
        for number in nums:
            if number in hashset:
                return True
            
            hashset.add(number)
        
        return False