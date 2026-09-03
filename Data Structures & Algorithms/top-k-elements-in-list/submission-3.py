class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        # the optimal solution is o(n)
        # the solution im writing is o(n log n)

        sortedfreq = []

        for key, freq in freqs.items():
            sortedfreq.append((-freq, key))

        sortedfreq = sorted(sortedfreq)

        answer = []

        for freq, num in sortedfreq: 
            answer.append(num)

            if len(answer) == k:
                break

        return answer