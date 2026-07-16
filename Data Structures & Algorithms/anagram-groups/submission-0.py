class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = [] # each key creates empty list corresponding to each key val
            
            groups[key].append(word) # add word to corresponding key list

        return list(groups.values())
