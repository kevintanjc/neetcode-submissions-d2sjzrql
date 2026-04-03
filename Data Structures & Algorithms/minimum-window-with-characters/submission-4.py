from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        table = Counter(t)
        have = {}        
        left = 0
        shortest_output = ""
        count = len(table)
        satisfied = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            if ch in table and have[ch] == table[ch]:
                satisfied += 1

            while satisfied == count:
                window = s[left : right + 1]

                if shortest_output == "" or len(window) < len(shortest_output):
                    shortest_output = window

                have[s[left]] -= 1

                if s[left] in table and have[s[left]] < table[s[left]]:
                    satisfied -= 1

                left += 1

        return shortest_output

        

            
