class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)

        for index in range(len(temperatures)-1, -1, -1):
            while temps and temperatures[index] >= temperatures[temps[-1]]:
                temps.pop()
            
            if temps:
                res[index] = temps[-1] - index
            
            temps.append(index)
        
        return res