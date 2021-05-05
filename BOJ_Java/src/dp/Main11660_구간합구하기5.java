package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11660_구간합구하기5 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] numbers = new int[N][N];
		int[][] dp = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				numbers[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			dp[i][0] = numbers[i][0];
			for (int j = 1; j < N; j++) {
				dp[i][j] = dp[i][j - 1] + numbers[i][j];
			}
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine(), " ");
			int sy = Integer.parseInt(st.nextToken()) - 1;
			int sx = Integer.parseInt(st.nextToken()) - 1;
			int ey = Integer.parseInt(st.nextToken()) - 1;
			int ex = Integer.parseInt(st.nextToken()) - 1;
			int answer = 0;
			
			for (int i = sy; i <= ey; i++) {
				if (sx > 0) {
					answer += (dp[i][ex] - dp[i][sx - 1]); 
				} else {
					answer += dp[i][ex];
				}
			}
			
			System.out.println(answer);
			
		}
		
	}

}
