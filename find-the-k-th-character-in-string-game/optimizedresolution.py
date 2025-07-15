class Solution:
    def kthCharacter(self, k :int) -> str:
        if k < 0 or k > 500:
            return "valor inválido"
        
        realist = ["a"]
        
        while len(realist) < k:
            newlist = []
            for j in realist:
                newlist.append(chr((((ord(j) - ord("a"))+1) % 26) + ord("a")))

            realist += newlist
        return realist[k - 1]
    
s = Solution()
print(s.kthCharacter(5))
