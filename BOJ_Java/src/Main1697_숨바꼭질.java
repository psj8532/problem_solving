import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Main1697_숨바꼭질 {
	private static int s,e,d;
	private static boolean[] visited;
	private static Queue<int[]> q;
	public static int bfs(int start, int goal, int depth) {
		int left,right,T,h;
		q = new LinkedList<>();
		q.offer(new int[] {start,depth});
		visited = new boolean[100001];
		visited[start] = true;
		while (!q.isEmpty()) {
			int[] here = q.poll();
			h = here[0];
			depth = here[1];
			if (h == goal) {
				return depth;
			}
			left = h - 1;
			right = h + 1;
			T = 2 * h;
			if (left >= 0 && !visited[left]) {
				q.offer(new int[] {left,depth+1});
				visited[left] = true;
			}
			if (right <= 100000 && !visited[right]) {
				q.offer(new int[] {right,depth+1});
				visited[right] = true;
			}
			if (T <= 100000 && !visited[T]) {
				q.offer(new int[] {T,depth+1});
				visited[T] = true;
			}
			
		}
		return depth;
	}
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		s = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		d = bfs(s,e,0);
		
		System.out.println(d);
	}

}
