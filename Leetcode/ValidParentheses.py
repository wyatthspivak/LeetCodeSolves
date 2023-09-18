class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_stack = []
        for i in range(len(s)):
            paren = s[i]
            if paren == '(' or paren == '{' or paren == '[':
                paren_stack.append(paren)
            elif (paren == ')' or paren == '}' or paren == ']') and paren_stack:
                open_paren = paren_stack.pop()
                if open_paren == '(' and paren == ')':
                    continue
                if open_paren == '{' and paren == '}':
                    continue
                if open_paren == '[' and paren == ']':
                    continue
                return False

            else:
                return False
        if paren_stack:
            return False
        else:
            return True


test = Solution()

print(test.isValid("){"))
