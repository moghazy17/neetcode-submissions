class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lw1 = len(word1)
        lw2 = len(word2)
        lsw = min(lw1, lw2)

        ans = ""
        
        for i in range(lsw):
            ans+=word1[i]
            ans+=word2[i]

        if lw1 > lw2:
            return ans+word1[lw2:]
        
        return ans+word2[lw1:]
        