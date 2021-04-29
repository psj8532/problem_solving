package combinatorics;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main15663_N과M9 {
	
	private static List<ArrayList<Integer>> perm = new ArrayList<ArrayList<Integer>>();
	
	private static void permutation(int depth, int[] a, int permSize, int totalSize, int[] sortedNumbers) {
		if (depth == permSize) {
			ArrayList<Integer> temp = new ArrayList<Integer>();
			for (int i = 0; i < permSize; i++) {
				temp.add(sortedNumbers[a[i]]);
			}
			if (!perm.contains(temp)) {
				perm.add(temp);
			};
		} else {
			boolean[] inPerm = new boolean[totalSize];
			
			for (int i = 0; i < depth; i++) {
				inPerm[a[i]] = true;
			}
			
			int[] c = new int[totalSize];
			int cnt = 0;
			for (int i = 0; i < totalSize; i++) {
				if (!inPerm[i]) {
					c[cnt++] = i;
				}
			}
			
			for (int i = 0; i < cnt; i++) {
				a[depth] = c[i];
				permutation(depth + 1, a, permSize, totalSize, sortedNumbers);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		int[] numbers = new int[N];
		for (int i = 0; i < N; i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(numbers);
		int[] a = new int[M];
		permutation(0, a, M, N, numbers);
		perm.forEach(arr -> {
			for (int num : arr) {
				System.out.print(num + " ");
			}
			System.out.println();
		});
		
	}

}
