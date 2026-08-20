class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = [] #creating string into list of strings
        i = 0 #used to find next encoded section

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j]) # length equals num before '#'
            start = j + 1 #actual string starts after j
            end = start + length

            result.append(s[start:end])
            i = end # new start is end of first section
        return result