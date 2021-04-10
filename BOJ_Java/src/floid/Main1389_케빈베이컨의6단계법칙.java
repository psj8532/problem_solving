package floid;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main1389_케빈베이컨의6단계법칙 {
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N =  Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int s, e, cost;
		int INF = 987654321;
		int minBacon = INF, answer = INF;
		int kevinBacon;
		
		int[][] relation = new int[N + 1][N + 1];
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				relation[i][j] = INF;
			}
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			relation[s][e] = 1;
			relation[e][s] = 1;
		}
		for (int i = 1; i <= N; i++) {
			relation[i][i] = 1;
		}
		for (int m = 1; m <= N; m++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					cost = relation[i][m] + relation[m][j];
					if (cost < relation[i][j]) {
						relation[i][j] = cost;
						relation[j][i] = cost;
					}
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			kevinBacon = 0;
			for (int j = 0; j <= N; j++) {
				kevinBacon += relation[i][j];
			}
			if (kevinBacon < minBacon) {
				answer = i;
				minBacon = kevinBacon;
			}
		}
		
		System.out.println(answer);
		
	}

}
