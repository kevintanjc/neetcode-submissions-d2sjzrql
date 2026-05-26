class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_order = sorted(s1)
        p1 = 0
        p2 = s1_len - 1

        while p2 < len(s2):
            
            substr_order = sorted(s2[p1:p2 + 1])
            if s1_order == substr_order:
                return True
            else:
                p2 += 1
                p1 += 1

        return False

                            



