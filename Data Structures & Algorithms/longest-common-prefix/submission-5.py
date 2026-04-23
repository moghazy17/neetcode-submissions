class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        lcp = len(ref)

        for i in range(1, len(strs)):
            w = strs[i]
            w_len = len(w)

            if w_len == 0: return ""

            for j in range(lcp):
                if j < w_len and ref[j] != w[j]:
                    lcp = j
                    break
            
            lcp = min(lcp, w_len)

            
        return ref[:lcp]

            




