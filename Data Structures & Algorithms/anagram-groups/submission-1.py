class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs: #for loop to go through all words in given strs list
            count = [0] * 26 #count = arr with 26 spots for alpha

            for char in word: #for loop to iterate through chars of each word
                index = ord(char) - ord('a') # index of each char accounting for ascii placement
                count[index] += 1 # if char exists, go to index and update count

            key = tuple(count) # immutable tuple for key

            if key not in groups: # if key hasn't been seen
                groups[key] = [] # create new sublist for the key
            
            groups[key].append(word) # add word into new sublist since sublists have all been created

        return list(groups.values()) # need to return all values as a list
        