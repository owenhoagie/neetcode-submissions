class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums))]
        for num, freq in count.items():
            bucket[freq-1].append(num)

        klargest = []
        current = 0
        for freqs in reversed(bucket):
            for num in freqs:
                klargest.append(num)
                current += 1
                
                if current == k:
                    return klargest


        return klargest