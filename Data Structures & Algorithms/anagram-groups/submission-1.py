class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in anagram_dic:
                anagram_dic[key].append(s)
            else:
                anagram_dic[key] = [s]
        
        return list(anagram_dic.values())

