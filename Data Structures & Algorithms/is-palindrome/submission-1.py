class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        new=""
        l=len(s)-1
        for i in range(l,-1,-1):
            new += s[i]
        return new==s