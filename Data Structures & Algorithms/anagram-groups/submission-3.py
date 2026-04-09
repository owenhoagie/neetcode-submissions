class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
        
            count = tuple(count)
            if count in group:
                group[count].append(word)
            else:
                group[count] = [word]

        return list(group.values())
