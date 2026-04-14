class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        ref = strs[0]
        
        def checkLCP(s1:str, s2:str):
            flag = min(len(s1), len(s2))
            for i in range(flag):
                if s1[i] != s2[i]:
                    return i
            return flag
        
        lcp_index = 201
        for i in strs:
            lcp_index = min(checkLCP(ref, i), lcp_index)
        
        return ref[:lcp_index]


