class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        count = [0] * 26
        
        for n in range(len(t)):
            count[ord(s[n]) - ord('a')] += 1
            count[ord(t[n]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True