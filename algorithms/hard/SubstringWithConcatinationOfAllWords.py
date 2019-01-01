class Solution:
    def findSubstring(self, s, words):
        """
        Given a string, s, and a list of words, words, that are all of the same
        length. Find all starting indices of substring(s) in s that is a 
        concatenation of each word in words exactly once and without any 
        intervening characters.
        
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        substring_len = len(words[0])
        combined_substring_len = len(words) * substring_len
        if len(s) < combined_substring_len:
            return []
        
        # Maintains the number of times a substring occurs in words
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Records the starting indices of substring(s) in s that are a 
        # concatenation of all the strings in words
        occurences = []
        
        # Iterates through all possible substrings of length 
        # combined_substring_len in s
        for i in range(len(s) - combined_substring_len + 1):
            words_seen = word_count.copy()
            words_not_seen = set(words)
            
            j = i
            while j < (i + combined_substring_len):
                substring = s[j:j + substring_len]
                if substring in words_seen:
                    words_seen[substring] -= 1
                else:
                    break
                
                # If a substring occurs too many times, break
                if words_seen[substring] < 0:
                    break
                j += substring_len
            
            if j == (i + combined_substring_len):
                occurences.append(i)
        return occurences

solution = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

print(s)
print(words)
print(solution.findSubstring(s, words))

