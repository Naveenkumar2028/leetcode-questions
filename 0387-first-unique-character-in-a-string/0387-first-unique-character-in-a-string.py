class Solution(object):
    def firstUniqChar(self, s):
      

        frequency = {}

        for ch in s:
            frequency[ch] = frequency.get(ch, 0) + 1

        for ch in s:
            if frequency[ch] == 1:
                return s.index(ch)
                break
        return -1

        