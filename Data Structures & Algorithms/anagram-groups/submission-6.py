class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        baseline = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            res = tuple(count)
            baseline[res].append(word)
        
        result = []

        for index in baseline:
            result.append(baseline[index])

        return result