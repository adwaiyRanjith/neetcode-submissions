class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.rstrip()
        count = 0
        for i in range(len(string)):
            if (string[len(string) - 1 - i] != " "):
                count +=1
            else:
                break
        return count