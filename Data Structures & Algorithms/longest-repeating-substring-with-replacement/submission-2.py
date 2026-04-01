class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        unique_letters = set(ltr for ltr in s)
        
        for letter_frequent in unique_letters:
            left_index = 0
            k_left = k

            for right_index in range(len(s)):
                if s[right_index] != letter_frequent:
                    k_left -= 1
                
                while k_left < 0:
                    if s[left_index] != letter_frequent:
                        k_left += 1
                    left_index += 1
                
                ans = max(ans, right_index - left_index + 1)
        
        return ans