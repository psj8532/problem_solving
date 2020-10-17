import java.util.*;
import java.io.*;

public class Main2606_바이러스 {
	private static int N, M;
	private static int s, e;
	private static int cnt = 0;
	private static int[][] adj;
	private static boolean[] visited;
	
	public static void dfs(int h) {
		for (int n=1; n<N+1; n++) {
			if (!visited[n] && adj[h][n] == 1) {
				cnt ++;
				visited[n] = true;
				dfs(n);
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(br.readLine());
		adj = new int[N+1][N+1];
		visited = new boolean[N+1];
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			adj[s][e] = 1;
			adj[e][s] = 1;
		}
		visited[1] = true;
		dfs(1);
		
		System.out.println(cnt);
	}

}
