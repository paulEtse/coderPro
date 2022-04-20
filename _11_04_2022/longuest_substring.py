#!/usr/bin/python3
class Solution:
    def lengthOfLongestSubstring(self, s):
        current_str_start = 0
        max_length = 0
        for i in range(len(s)):
            current_char = s[i]
            if current_char in s[current_str_start:i]:
                if i - current_str_start > max_length:
                    max_length = i - current_str_start
                current_str_start = s[0:i].rindex(current_char) + 1
        return min(max_length, len(s))
