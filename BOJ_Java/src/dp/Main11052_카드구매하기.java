package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11052_카드구매하기 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		int[] price = new int[N+1];
		int half, sum;
		for (int i = 1; i <= N; i++) {
			price[i] = Integer.parseInt(st.nextToken());
		}
		int[] dp = new int[N+1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (j < i) continue;
				else if (j == i && dp[j] < price[i]) dp[j] = price[i];
				else {
					half = j / 2;
					for (int k = 1; k <= half; k++) {
						sum = dp[k] + dp[j-k];
						if (sum > dp[j]) dp[j] = sum;
					}
						
				}
			}
		}
		
		System.out.println(dp[N]);
	}

}
