class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        # if char not in count_s, value of count of char is 0 + 1 because this is first iteration of this letter

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        if count_t == count_s:
            return True
        else:
            return False