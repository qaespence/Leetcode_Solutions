import java.util.HashMap;

public class RomanToInteger {

	public int RomanToIntegerSolution(String s) {
		int result = 0;
		char[] charArray = s.toCharArray();
		
		HashMap<Character,Integer> symbols = new HashMap<>();
		symbols.put('I', 1);
		symbols.put('V', 5);
		symbols.put('X', 10);
		symbols.put('L', 50);
		symbols.put('C', 100);
		symbols.put('D', 500);
		symbols.put('M', 1000);
		
		for (int i = 0; i < charArray.length; i++) {
			if(i == charArray.length - 1) {
				result += symbols.get(charArray[i]);
			} else if (symbols.get(charArray[i]) >= symbols.get(charArray[i + 1])) {
				result += symbols.get(charArray[i]);
			} else {
				result += symbols.get(charArray[i + 1]) - symbols.get(charArray[i]);
				i++;
			}
		}
		return result; 
	    }
}
