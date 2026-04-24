class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPal(l, r):
            while l < r:
                if s[l] != s[r]: 
                    return False
                l+=1
                r-=1
            return True

            
        r = len(s) - 1 
        l = 0

        while l < r:
            if s[l] != s[r]:
                return checkPal(l, r-1) or checkPal(l+1, r)

            l+=1
            r-=1
        return True 


