class Solution:
    def longestValidParentheses(self, s):
        """
        Given a string containing just the characters '(' and ')', find the 
        length of the longest valid (well-formed) parentheses substring.
        
        :type s: str
        :rtype: int
        """
        open_paren_count = 0
        max_len = 0  # length of longest well-formed parentheses substring
        cur_len = 0  # length of the current well-formed parentheses substring
        start_idx = 0  # start of the current well-formed parentheses substring
        for i, c in enumerate(s):
            if c == '(':
                open_paren_count += 1
            else:
                open_paren_count -= 1
                
                # Unmatched closed parenthesis, reset variables
                if open_paren_count < 0:
                    max_len = max(max_len, cur_len)
                    cur_len = 0
                    start_idx = i + 1
                    open_paren_count = 0
                
                # A well-formed parenthesis substring has terminated
                if open_paren_count == 0:
                    cur_len += i - start_idx + 1
                    max_len = max(max_len, cur_len)
                    start_idx = i + 1
        
        if open_paren_count > 0:
            # Extract the portion of the end of the string with a repeated open
            # parenthesis
            unmatched_open_string = s[start_idx:]
            
            # Create a flipped version of the string
            # Example: '(()' -> '())'
            reversed_substring = unmatched_open_string[::-1]
            flipped_substring = ""
            d = {'(':')', ')':'('}
            last_closed_paren = 0
            for i in range(len(reversed_substring)):
                if d[reversed_substring[i]] == ')':
                    last_closed_paren = i
                flipped_substring += d[reversed_substring[i]]
            
            longest_paren = self.longestValidParentheses(flipped_substring[:i])
            max_len = max(max_len, longest_paren)
        
        return max_len
        
s = Solution()
string = '(()'
print(string)
print(s.longestValidParentheses(string))
