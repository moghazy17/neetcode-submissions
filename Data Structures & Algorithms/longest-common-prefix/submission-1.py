class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        lcp = len(ref)

        for i in range(1, len(strs)):
            w = strs[i]
            w_len = len(w)
            for j in range(lcp):
                if j < w_len and ref[j] != w[j]:
                    lcp = j
            
        return ref[:lcp]

            




