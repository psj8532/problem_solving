import java.util.*;
import java.io.*;

public class Main2178_미로탐색 {
	static int N,M;
	static int[][] maze;
	static boolean[][] visited;
	static Queue<int[]> q;
	static int[][] direct = {
			{-1,0},
			{0,1},
			{1,0},
			{0,-1},
	};
	public static int bfs(int y, int x, int depth) {
		int ny, nx;
		q = new LinkedList<>();
		q.offer(new int[] {y,x,depth});
		visited[y][x] = true;
		
		while (!q.isEmpty()) {
			int[] position = q.poll();
			depth = position[2];
			for (int i=0; i<4; i++) {
				ny = position[0] + direct[i][0];
				nx = position[1] + direct[i][1];
				if ((ny == N - 1) && (nx == M - 1)) {
					return depth + 1;
				} else if ((0<=ny && ny<N && 0<=nx && nx<M) && !visited[ny][nx] && maze[ny][nx] == 1) {
					q.offer(new int[] {ny,nx,depth+1});
					visited[ny][nx] = true;
				}
			}
		}
		return 0;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		maze = new int[N][M];
		visited = new boolean[N][M];
		int i,j,depth;
		
		
		for (i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			String line = st.nextToken();
			for (j=0; j<M; j++) {
				maze[i][j] = line.charAt(j) - '0';
			}
		}
		
		depth = bfs(0, 0, 1);
		System.out.println(depth);

	}

}
