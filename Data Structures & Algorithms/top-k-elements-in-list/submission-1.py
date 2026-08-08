class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for i in range(len(nums))]
        for num in count:
            bucket[count[num]-1].append(num)
        
        answer = []
        for freq in bucket[::-1]:
            for num in freq:
                answer.append(num)
                if len(answer) == k:
                    return answer


        