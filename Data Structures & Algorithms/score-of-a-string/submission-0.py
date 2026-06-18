class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        cur, nex = 0, 1
        while (nex < len(s)):
            score += abs(ord(s[nex]) - ord(s[cur]))
            cur += 1
            nex += 1
        return score