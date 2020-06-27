import java.util.*;
import java.io.*;

public class Main17472_다리만들기2 {
	static int N,M;
	static int[][] matrix;
	static int[][] adj;
	static boolean[] mst;
	static int[] key;
	static boolean[][] visited;
	static Queue<int[] > q;
	static int[][] direct = {
			{-1,0},
			{0,1},
			{1,0},
			{0,-1},
	};
	public static void change(int y, int x, int number) {
		int ny,nx,dir;
		q = new LinkedList<>();
		q.offer(new int[] {y,x});
		visited[y][x] = true;
		matrix[y][x] = number;
		while(!q.isEmpty()) {
			int[] here = q.poll();
			for (dir=0; dir<4; dir++) {
				ny = here[0] + direct[dir][0];
				nx = here[1] + direct[dir][1];
				if (0 <= ny && ny<N && 0 <= nx && nx < M && matrix[ny][nx] == 1 && !visited[ny][nx]) {
					matrix[ny][nx] = number;
					q.offer(new int[] {ny,nx});
					visited[ny][nx] = true;
				}
			}
		}
	}
	
	public static void bfs(int y, int x, int c, int v) {
		int ny,nx,dir;
		q = new LinkedList<>();
		for (dir=0; dir<4; dir++) {
			ny = y + direct[dir][0];
			nx = x + direct[dir][1];
			if (0 <= ny && ny<N && 0 <= nx && nx < M && matrix[ny][nx]==0) {
				q.offer(new int[] {ny,nx,c+1,dir});
			}
		}
		while (!q.isEmpty()) {
			int[] here = q.poll();
			ny = here[0] + direct[here[3]][0];
			nx = here[1] + direct[here[3]][1];
			c = here[2];
			if (0 <= ny && ny<N && 0 <= nx && nx < M && matrix[ny][nx]>0 && matrix[ny][nx]!=v && c >= 2 && c < adj[v][matrix[ny][nx]]) {
				adj[v][matrix[ny][nx]] = c;
				adj[matrix[ny][nx]][v] = c;
			} else if (0 <= ny && ny<N && 0 <= nx && nx < M && matrix[ny][nx] == 0) {
				q.offer(new int[] {ny,nx,c+1,here[3]});
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		matrix = new int[N][M];
		visited = new boolean[N][M];
		int i,j,num,min,result,cnt,u;
		for (i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (j=0; j<M; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		num = 0;
		for (i=0; i<N; i++) {
			for (j=0; j<M; j++) {
				if (matrix[i][j] > 0 && !visited[i][j]) {
					num ++;
					change(i,j,num);
				}
			}
		}
		
		adj = new int[num+1][num+1];
		for (i=0; i<num+1; i++) {
			for (j=0; j<num+1; j++) {
				adj[i][j] = 1000;
			}
		}
		for (i=0; i<N; i++) {
			for (j=0; j<M; j++) {
				if (matrix[i][j] > 0) {
					bfs(i,j,0,matrix[i][j]);
				}
			}
		}
		mst = new boolean[num+1];
		key = new int[num+1];
		for (i=0; i < num+1; i++) {
			key[i] = 1000;
		}
		key[1] = 0;
		result = 0;
		cnt = 0;
		u = 0;
		while (cnt<num) {
			min = 1000;
			for (i=1; i<num+1; i++) {
				if (!mst[i] && key[i] < min) {
					min = key[i];
					u = i;
				}
			}
			mst[u] = true;
			result += min;
			cnt ++;
			for (int w=1; w<num+1; w++) {
				if (!mst[w] && adj[u][w] < key[w]) {
					key[w] = adj[u][w];
				}
			}
		}
		if (result<1000) {
			System.out.println(result);
		} else {
			System.out.println(-1);
		}
		
	}

}
