class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        newer = s.split()
        answer = len(newer[len(newer) - 1])
        return answer
            