class Solution:
    def getExpected(self, s: str):
        if s == '(':
            return ')'
        elif s == '[':
            return ']'
        elif s == '{':
            return '}'
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = deque()
        for el in s:
            if el == '(' or el == '[' or el == '{':
                stack.append(el)
            elif len(stack) > 0:
                top = stack.pop()
                if el != self.getExpected(top):
                    return False
            else:
                return False
        return len(stack) == 0
