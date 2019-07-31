import java.util.ArrayList;

public class LargestThreeElementsOfList {
	public ArrayList<Integer> LargestElementsOfList(ArrayList<Integer> data, int N) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		
		for (int i = 0; i < N; i++) {
			int max = data.get(0);
			int maxloc = 0;
			for (int j = 1; j < data.size(); j++) {
				if (max < data.get(j)) {
					max = data.get(j);
					maxloc = j;
				}
			}
			result.add(max);
			data.remove(maxloc);
		}
		
		return result;
	}
}
