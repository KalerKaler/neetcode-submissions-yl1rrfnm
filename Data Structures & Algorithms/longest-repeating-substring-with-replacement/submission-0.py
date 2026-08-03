class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0
        res = 0
        charCounts = [0] * 26

        for r in range(len(s)):

            charCounts[ord(s[r]) - 65] += 1
            mostFreq = max(charCounts)

            while sum(charCounts) - mostFreq > k:
                charCounts[ord(s[l]) - 65] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
