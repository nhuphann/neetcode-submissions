class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
            #5#hello2#hi
        return res 
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length =  int(s[i:j])  
            i = j + 1
            #h
            res.append(s[i:i + length])
            # 2 + 5
            # 2:7
            i += length
            # 2 or index = 7
        return res

