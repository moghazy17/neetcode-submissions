class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(ref), len(strs[i])):
                if ref[j] != strs[i][j]:
                    break
                j+=1
            ref = ref[:j]

        return ref


            




