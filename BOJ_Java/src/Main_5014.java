import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Queue;

public class Main_5014 {
	private static int F, S, G, U, D;
	private static boolean[] visited;
	private static Queue<int []> q;
	
	public static int bfs(int depth) {
		int h, n;
		q = new LinkedList<>();
		visited = new boolean[F+1];
		q.offer(new int[] {S,depth});
		visited[S] = true;
		
		while(!q.isEmpty()) {
			int[] here = q.poll();
			h = here[0];
			depth = here[1];
			if (h == G) {
				return depth;
			}
			n = h + U;
			if (1 <= n && n<=F && !visited[n]) {
				q.offer(new int[] {n, depth+1});
				visited[n] = true;
			}
			n = h - D;
			if (1 <= n && n<=F && !visited[n]) {
				q.offer(new int[] {n, depth+1});
				visited[n] = true;
			}
		}
		return -1;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		F = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		G = Integer.parseInt(st.nextToken());
		U = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		int result;
		
		result = bfs(0);
		if (result == -1) {
			System.out.println("use the stairs");
		} else {
			System.out.println(result);
		}
	}

}
