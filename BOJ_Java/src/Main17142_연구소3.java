import java.util.*;
import java.io.*;

public class Main17142_연구소3 {
	static int N, M;
	static int[][] matrix;
	static int[][] direct = {
			{-1,0},
			{0,1},
			{1,0},
			{0,-1},
	};
	static int[] comb;
	static int[][] virus;
	static int top = 0;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		matrix = new int[N][N];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j=0; j<N; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
	}

}
