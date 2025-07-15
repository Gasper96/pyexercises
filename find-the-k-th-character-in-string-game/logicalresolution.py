class Solution:
    def kthCharacter(self, k :int) -> str:
        if k < 0 or k > 500:
            return -1
        
        realist = ["a"]
        newlist = []
        listalf = ["a","b","c","d",
                   "e","f","g","h",
                   "i","j","k","l",
                   "m","n","o","p",
                   "q","r","s","t",
                   "u","v","w","x","y","z","a"]
        

        for i in range(9):
            newlist = []
            for j in realist:
                newlist.append(listalf[listalf.index(j) + 1])

            realist = realist + newlist

        return "".join(newlist)
    
s = Solution()
print(s.kthCharacter(2))
