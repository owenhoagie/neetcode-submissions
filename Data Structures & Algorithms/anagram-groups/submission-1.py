class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in groups:
                groups[sort].append(word)
            else:
                groups[sort].append(word)

        answer = []
        for lists in groups.values():
            answer.append(lists)

        return answer