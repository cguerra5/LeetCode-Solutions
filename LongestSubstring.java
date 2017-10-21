import java.util.HashSet;
/**
 * Problem Title: Longest Substring Without Repeating Characters
 * 
 * Given a string, finds the length of the longest substring without repeating
 * characters.
 * Examples:
 * -Given "abcabcbb", the answer is "abc", which the length is 3
 * -Given "bbbbb", the answer is "b", with the length of 1.
 * -Given "pwwkew", the answer is "wke", with the length of 3. Note that the 
 *  answer must be a substring, "pwke" is a subsequence and not a substring.
 *
 * @author Carlos R. Guerra
 */
class LongestSubstring
{

	public static void main(String args[])
	{
		String test = "abcabc";
		System.out.println(lengthOfLongestSubstring(test) + "");
	}

	public static int lengthOfLongestSubstring(String s)  
	{
		int maxLength = 0;
		HashSet<Character> repeatedChars = new HashSet<>();
		
		int curSize = 0;
		for(char c : s.toCharArray()) {
			if(!(repeatedChars.contains(c))) {
				curSize++;
				repeatedChars.add(c);
			} else {
				maxLength = (curLength > maxLength) ? curLength : maxLength;
				while(s[startIndex] != s[i]) {
					repeatedChars.remove(s[startIndex]);
					startIndex++;
					curLength--;
				}
				startIndex++;
				curLength--;
			}
		}
		return maxLength;
	}
}
