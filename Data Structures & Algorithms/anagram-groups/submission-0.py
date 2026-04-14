class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        ans = []

        for s in strs:
            key = "".join(sorted(s))
            if key in anagram_dic:
                ans[anagram_dic[key]].append(s)
            else:
                anagram_dic[key] = len(anagram_dic)
                ans.append([s])
        
        return ans

