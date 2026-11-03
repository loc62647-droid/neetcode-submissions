class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if abs(ord(s[i]) - ord(stack[-1])) != 32:
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)