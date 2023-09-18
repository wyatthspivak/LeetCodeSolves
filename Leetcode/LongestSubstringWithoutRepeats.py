class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_start = 0

        char_freq = {}

        for window_end in range(len(s)):
            next_char = s[window_end]

            if next_char not in char_freq:
                char_freq[next_char] = 0

            char_freq[next_char] += 1

            # if the frequency of the new character in the string is greater than 1, then shrink the window
            while char_freq[next_char] > 1:
                start_char = s[window_start]
                char_freq[start_char] -= 1
                window_start += 1

            # now find the length of the current string and see if it is a new max length
            curr_length = window_end - window_start + 1

            max_length = max(curr_length, max_length)

        return max_length

sol = Solution()

print(sol.lengthOfLongestSubstring("absjkl"))
