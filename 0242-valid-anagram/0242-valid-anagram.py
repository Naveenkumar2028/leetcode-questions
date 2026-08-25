class Solution(object):
    def isAnagram(self, s, t):
        

        s= s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        if sorted(s) == sorted(t):
            return True
        else:
            return False