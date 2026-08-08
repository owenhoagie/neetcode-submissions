class Solution:

    def encode(self, strs: List[str]) -> str:
        new = []
        for word in strs:
            temp = []
            for char in word:
                temp.append(str(ord(char)) + '.')
            temp.append('-')
            new.append(''.join(temp))
        print(new)
        return ''.join(new)

    def decode(self, s: str) -> List[str]:
        result = []
        run = []
        num = []
        for char in s:
            if char == ".":
                code = chr(int(''.join(num)))
                num = []
                run.append(code)
            elif char == "-":
                result.append(''.join(run))
                run = []
            else:
                num.append(char)
        return result

