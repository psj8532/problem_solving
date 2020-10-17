import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;

public class Main2606_바이러스_스택 {
	private static int N, M;
	private static int s, e;
	private static int cnt = -1;
	private static int[][] adj;
	private static boolean[] visited;
	private static Stack <Integer> stack;
	
	public static void dfs(int h) {
		stack = new Stack<Integer>();
		stack.push(h);
		while (!stack.isEmpty()) {
			h = stack.pop();
			if (!visited[h]) {
				visited[h] = true;
				cnt++;
				for (int n=N; n>0; n--) {
					if (!visited[n] && adj[h][n] == 1) {
						stack.push(n);
					}
				}
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
		dfs(1);
		
		System.out.println(cnt);
	}

}
