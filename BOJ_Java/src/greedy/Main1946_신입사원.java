package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main1946_신입사원 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int T = Integer.parseInt(st.nextToken());
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int answer = 0;
			int[] document = new int[N + 1];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int docRanking = Integer.parseInt(st.nextToken());
				int intRanking = Integer.parseInt(st.nextToken());
				document[docRanking] = intRanking;
				
			}
			
			int topInterview = document[1];
			for (int i = 1; i <= N; i++) {
				if (document[i] <= topInterview) {
					answer++;
					topInterview = document[i];
				}
			}
			
			System.out.println(answer);
		}
		

	}

}
