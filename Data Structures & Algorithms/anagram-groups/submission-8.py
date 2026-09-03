class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        baseline = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            baseline[tuple(count)].append(word)
    
        for index in baseline:
            result.append(baseline[index])

        return result