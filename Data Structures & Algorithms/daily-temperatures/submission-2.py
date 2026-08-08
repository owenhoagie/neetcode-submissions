class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while temps and temperatures[i] >= temperatures[temps[-1]]:
                temps.pop()

            if temps:
                res[i] = temps[-1] - i
            
            temps.append(i)

        return res