package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main10162_전자레인지 {
	
	private static int BUTTON_CNT = 3;
	private static int[] button = {300, 60, 10};
	private static int[] answer = new int[BUTTON_CNT];
	
	private static boolean dfs(int depth, int remainder, boolean isEnd) {
		if (depth == BUTTON_CNT) {
			return true;
		}
		else {
			int timeUnit = button[depth];
			int bestFit = remainder / timeUnit;
			int temp = answer[depth];
			answer[depth] = bestFit;
			if (dfs(depth + 1, remainder - (timeUnit * bestFit), isEnd)) {
				return true;
			}
			answer[depth] = temp;
			return isEnd;
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		if (T % 10 > 0) {
			System.out.println(-1);
		} else {
			dfs(0, T, false);
			for(int ans : answer) {
				System.out.print(ans + " ");
			}
		}
		
		

	}

}
