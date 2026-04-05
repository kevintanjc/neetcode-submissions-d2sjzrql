class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dp(s, t):
            if s == "":
                return True
            elif t == "":
                return False
            elif len(s) > len(t):
                return False

            if s[0] == t[0]:
                return dp(s[1:], t[1:])
            else:
                return dp(s, t[1:])
        return dp(s,t)