import java.util.*;
import java.io.*;

public class Main1260_DFS와BFS {
	public static int N,M,start;
	
	public static void dfs(int[][] adj) {
		int next, here;
		int[] stack = new int[1000000];
		int[] visited = new int[N+1];
		int top = 0;
		stack[top] = start;
		
		while (top != -1) {
			here = stack[top];
			top--;
			if (visited[here] == 0) {
				visited[here] = 1;
				System.out.print(here + " ");
				for (next=N; next>0; next--) {
					if (adj[here][next] != 0 && visited[next] == 0) {
						top += 1;
						stack[top] = next;
					}
				}
			}
		}
		System.out.println();
	}
	
	public static void bfs(int[][] adj) {
		Deque<Integer> deq = new ArrayDeque<Integer>();
		int[] visited = new int[N+1];
		int here, next;
		deq.add(start);
		visited[start] = 1;
		System.out.print(start + " ");
		while (!deq.isEmpty()) {
			here = deq.pollFirst();
			for (next=1; next<N+1; next++) {
				if (adj[here][next]!=0 && visited[next]==0) {
					deq.add(next);
					visited[next] = 1;
					System.out.print(next + " ");
				}
			}
		}
		
	}
	
	public static void main(String[] args) throws Exception {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int i,s,e;
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		start = Integer.parseInt(st.nextToken());
//		N = sc.nextInt();
//		M = sc.nextInt();
//		start = sc.nextInt();	
		int[][] adj = new int[N+1][N+1];
	
		for (i=0; i<M; i++) {
//			s = sc.nextInt();
//			e = sc.nextInt();
			st = new StringTokenizer(br.readLine(), " ");
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			adj[s][e] = 1;
			adj[e][s] = 1;
		}
		dfs(adj);
		bfs(adj);
	
	}

}
