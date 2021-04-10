package prime;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main9020_골드바흐의추측 {
	
	private static List<Integer> primeList = new ArrayList<Integer>();
	
	private static boolean[] filterPrime() {
		int MAX_SIZE = 10000;
		boolean[] primes = new boolean[MAX_SIZE + 1];
		primes[0] = true;
		primes[1] = true;
		for (int i = 2; i <= MAX_SIZE; i++) {
			if (primes[i]) continue;
			primeList.add(i);
			for (int j = i * 2; j <= MAX_SIZE; j += i) {
				if (primes[j]) continue;
				primes[j] = true;
			}
		}
		return primes;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int tc = Integer.parseInt(st.nextToken());
		int n, half, remainder;
		int[] answer = new int[2];
 		boolean[] primes = filterPrime();
		Collections.sort(primeList);
		for (int t = 0; t < tc; t++) {
			st = new StringTokenizer(br.readLine(), " ");
			n = Integer.parseInt(st.nextToken());
			half = n / 2;
			for (int num : primeList) {
				if (num > half) break;
				remainder = n - num;
				if (primes[remainder]) continue;
				answer[0] = num;
				answer[1] = remainder;
			}
			for (int ans : answer) {
				System.out.print(ans + " ");
			}
			System.out.println();
		}
		
	}

}
