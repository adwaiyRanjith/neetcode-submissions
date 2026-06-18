class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c.lower() for c in s if c.isalnum())
        first = 0
        last = len(string) - 1
        for i in range(len(string)//2):
            if (string[first] == string[last]):
                first += 1
                last -= 1
                continue
            return False
        return True
        