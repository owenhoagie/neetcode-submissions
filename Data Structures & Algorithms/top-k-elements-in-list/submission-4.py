class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        answer = []

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        bucket = [[] for i in range(len(nums))]

        for num, freq in freqs.items():
            bucket[freq-1].append(num)
        
        for bucketFreqs in bucket[::-1]:
            for num in bucketFreqs:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return answer