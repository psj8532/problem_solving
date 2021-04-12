package boj_past;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main14500_테트로미노 {
	
	private static int N, M;
	private static int[][] matrix;
	private static int[] dy = {-1,0,1,0};
	private static int[] dx = {0,1,0,-1};
	private static int MAX_DIRECTION = 4;
	private static int max = 0;
	
	private static int dfs(int y, int x, int depth, int sum, boolean[][] visited) {
		if (depth >= 4) {
			if (sum > max) max = sum;
			return depth;
		} 
		
		int ny, nx, nny, nnx;
		boolean jump = false;
		for (int dir = 0; dir < MAX_DIRECTION; dir++) {
			ny = y + dy[dir];
			nx = x + dx[dir];
			if (0 <= ny && ny < N && 0 <= nx && nx < M && !visited[ny][nx]) {
				visited[ny][nx] = true;
				jump = true;
				dfs(ny, nx, depth + 1, sum + matrix[ny][nx], visited);	
				visited[ny][nx] = false;
				
			}
			if (depth == 2 && jump) {
				for (int nDir = 0; nDir < MAX_DIRECTION; nDir++) {
					if (dir == nDir) continue;
					nny = y + dy[nDir];
					nnx = x + dx[nDir];
					if (0 <= nny && nny < N && 0 <= nnx && nnx < M && !visited[nny][nnx]) {
						dfs(nny, nnx, depth + 2, sum + matrix[ny][nx] + matrix[nny][nnx], visited);
					}
				}
				jump = false;
			}
		}
		return depth;
		
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
	N = Integer.parseInt(st.nextToken());
	M = Integer.parseInt(st.nextToken());
	
	matrix = new int[N][M];
	
	for (int i = 0; i < N; i++) {
		st = new StringTokenizer(br.readLine(), " ");
		for (int j = 0; j < M; j++) {
			matrix[i][j] = Integer.parseInt(st.nextToken());
		}
	}
	
	boolean[][] visited = new boolean[N][M];
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = true;
			dfs(i, j, 1, matrix[i][j], visited);
			visited[i][j] = false;
		}
	}
	
	System.out.println(max);
	
	}

}
