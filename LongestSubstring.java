import java.util.HashSet;

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
