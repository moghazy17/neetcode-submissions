class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()]).lower()
        while len(s) > 1:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]
        return True