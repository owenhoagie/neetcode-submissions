class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)

        if l <= 1:
            return l
        
        left = 0
        right = 1

        longest = 1
        length = 1
        cl = set(s[0])

        while right < l:
            if s[right] in cl:
                longest = max(longest, length)

                while s[left] != s[right]:
                    cl.remove(s[left])
                    length -= 1
                    left += 1

                cl.remove(s[left])
                length -= 1
                left += 1
            else:
                cl.add(s[right])
                right += 1
                length += 1

        return max(longest, length)
            

                

            
            