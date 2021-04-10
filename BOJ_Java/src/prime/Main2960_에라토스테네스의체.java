package prime;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2960_에라토스테네스의체 {
	
	private static int check(int n, int k) {
		boolean[] numbers = new boolean[n + 1] ;
		int cnt = 0;
		for (int i = 2; i <= n; i++) {
			if (numbers[i]) continue;
			for (int j = i; j <= n; j += i) {
				if (numbers[j]) continue;
				cnt++;
				if (cnt == k) return j;
				numbers[j] = true;
			}
		}
		return n;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int answer = check(N, K);
		
		System.out.println(answer);
	}

}
