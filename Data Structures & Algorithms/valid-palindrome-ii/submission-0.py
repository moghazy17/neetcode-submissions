class Solution:
    def validPalindrome(self, s: str) -> bool:
        r = len(s) - 1 
        l = 0
        deleted = False

        while l < r:
            if s[l] != s[r]:
                if deleted: 
                    return False
                else:
                    if s[r] == s[l+1]:
                        l+=1
                        deleted = True
                        continue
                    elif s[l] == s[r-1]:
                        deleted = True
                        r-=1
                        continue
                    else:
                        return False
            r-=1
            l+=1
        return True
            
                    
            



            
            

