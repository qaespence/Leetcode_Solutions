
public class DefangingAnIpAddress {

	public String DefangingAnIpAddressSolution(String address) {
		String result = new String("");
		for (char c: address.toCharArray()) {
			if (c == '.')
			{
				result += "[.]";
			} else {
				result += c;
			}
		}
		return result;
	}
}
