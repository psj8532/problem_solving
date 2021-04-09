package boj_past;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main17281_야구 {
	
	private static final int MAX_BATSMAN = 9;
	private static List<int[]> perm = new ArrayList<int[]>();
	private static final int[] customOrder = {1, 2, 3, 4, 5, 6, 7, 8};
	
	private static void permutation(int k, int[] a, int pSize, int totalSize) {
		if (k == pSize) {
			int[] p = new int[pSize];
			for (int i = 0; i < pSize; i++) {
				p[i] = a[i];
			}
			perm.add(p);
		} else {
			boolean[] inPerm = new boolean[totalSize];
			
			for (int i = 0; i < k; i++) {
				inPerm[a[i]] = true;
			}
			
			int[] c = new int[totalSize];
			int cnt = 0;
			
			for (int i = 0; i < totalSize; i++) {
				if (inPerm[i]) continue;
				c[cnt++] = i;
			}
			
			for (int i = 0; i < cnt; i++) {
				a[k] = c[i];
				permutation(k + 1, a, pSize, totalSize);
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int[][] scoreTable = new int[N][MAX_BATSMAN];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < MAX_BATSMAN; j++) {
				scoreTable[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int maxScore = 0;
		int[] a = new int[MAX_BATSMAN - 1];
		permutation(0, a, 8, 8);
		
		for (int[] p : perm) {
			List<Integer> order = new ArrayList<Integer>();
			for (int i = 0; i < MAX_BATSMAN - 1; i++) {
				if (i == 3) order.add(0);
				order.add(customOrder[p[i]]);
			}
			int innings = 0, score = 0, currBatsman = 0;
			while (innings < N) {
				int outCount = 0;
				List<Integer> base = new ArrayList<Integer>();
				
				while (outCount < 3) {
					int batsman = order.get(currBatsman);
					int hits = scoreTable[innings][batsman];
					if (hits == 0) {
						outCount++;
						
					} else if (hits == 4) {
						score += base.size() + 1;
						base = new ArrayList<Integer>();						
					} else {
						List<Integer> newBase = new ArrayList<Integer>();
						for (int runner : base) {
							int nextBase = runner + hits;
							if (nextBase >= 4) {
								score++;
							} else {
								newBase.add(nextBase);
							}
						}
						newBase.add(hits);
						base = newBase.stream().map(runner -> runner).collect(Collectors.toList());
						
					}
					
					currBatsman = (currBatsman + 1) % MAX_BATSMAN;
					
				}
				innings++;
				
			}
			if (score > maxScore) maxScore = score;
		}
		
		System.out.println(maxScore);
		
		
	}

}
