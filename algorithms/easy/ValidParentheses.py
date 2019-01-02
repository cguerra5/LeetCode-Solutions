class Solution:
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '['
        and ']', determine if the input string is valid.

        :param s: A string of the characters '(', ')', '{', '}', '[' and '['
        :type s: str
        :return: Whether or not a string s only contain brackets which are
                 closed by the same type of brackets and are closed in the
                 correct order
        :rtype: bool
        """
        stack = []
        open_bracket = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in open_bracket:
                stack.append(open_bracket[c])
            else:
                # If the stack is empty, then the close bracket does not have a
                # matching open bracket
                if (not stack) or (stack.pop() != c):
                    return False
        
        # If the stack is not empty, then there are unmatched open brackets
        return not stack

s = Solution()
string = "([)]"
print(s.isValid(string))
