# Given two strings "s" and "t", return true if "t" is an anagram of "s", and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    
    # Sorted solution --> Time complexity: O(nlogn)
    def is_anagram_sorted(self, string_original: str, anagram_to_validate: str) -> bool:
        return sorted(string_original) == sorted(anagram_to_validate)
    
    # Hash map solution -> Time complexity: O(s + t)
    def is_anagram_hash_map(self, string_original: str, anagram_to_validate: str) -> bool:
        if len(string_original) != len(anagram_to_validate):
            return False
        
        count_string_original, count_anagram_to_validate = {}, {}
        
        for character_position in range(len(string_original)):
            count_string_original[string_original[character_position]] = 1 + count_string_original.get(string_original[character_position], 0)
            count_anagram_to_validate[anagram_to_validate[character_position]] = 1 + count_anagram_to_validate.get(anagram_to_validate[character_position], 0)
        
        for character_position in count_string_original:
            if count_string_original[character_position] != count_anagram_to_validate.get(character_position, 0):
                return False
        
        return True