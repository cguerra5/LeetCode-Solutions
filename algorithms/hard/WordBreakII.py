class Solution:
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: List[str]
        """
        word_set = set(word_dict)
        substrings = {}
        for i in range(len(s)):
            if s[0:i + 1] in word_set:
                if i in substrings:
                    substrings[i].append(s[0:i + 1])
                else:
                    substrings[i] = [s[0:i + 1]]
            for key, lis in list(substrings.items()):
                substr = s[key + 1:i + 1]
                if substr in word_set:
                    if i in substrings:
                        substrings[i] += (list(map(lambda x: x + ' ' + substr, substrings[key])))
                    else:
                        substrings[i] = list(map(lambda x: x + ' ' + substr, substrings[key]))
        ans = []
        n = len(s)
        if n - 1 in substrings:
            for string in substrings[n - 1]:
                print(string)
                if len(string.replace(' ', '')) == n:
                    ans.append(string)
        return ans

sol = Solution()
s = 'catsanddog'
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(sol.wordBreak(s, word_dict))

