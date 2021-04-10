package backtracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main2023_신기한소수 {
	
	private static List<Integer> answer = new ArrayList<Integer>();
	
	private static boolean checkPrime(int n) {
		if (n == 0 || n == 1) {
			return false;
		}
		for (int i = 2; i <=  Math.sqrt(n); i++) {
			if (n % i == 0) return false;
		}
		return true;
		
	}
	
	private static void dfs(String number, int k, int N) {
		if (k == N) {
			answer.add(Integer.parseInt(number));
		} else {
			for (int i = 1; i <= 9; i++) {
				String num = number + Integer.toString(i);
				boolean check = checkPrime(Integer.parseInt(num)); 
				if (check) {
					dfs(num, k + 1, N);
				}
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		
		dfs("", 0, N);
		answer.forEach(num -> System.out.println(num));
		
	}

}
