class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=len(s)
        new=s[::-1]
        return new==s
        