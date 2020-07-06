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
	static int[][] comb;
	static int[] a;
	static int[][] virus;
	static int virusCount = 0;
	static int top = 0;
	static int[][] visited;
	static Queue<int[] > q;
	
	public static void combination(int index, int[] a) {
		if (index == M) {
			int[] temp = new int[M];
			for (int i=0; i<M; i++) {
				temp[i] = a[i];
			}
			for (int i=0; i<M; i++) {
				comb[top][i] = temp[i];
			}
			top ++;
		} else {
			int posi = 0;
			int cnt = 0;
			boolean[] inComb = new boolean[virusCount];
			for (int i=0; i<index; i++) {
				inComb[a[i]] = true;
			}
			for (int i=virusCount-1; i>-1; i--) {
				if (inComb[i]) {
					posi = i+1;
					break;
				}
			}
			int[] c = new int[virusCount];
			for (int i=posi; i<virusCount; i++) {
				if (!inComb[i]) {
					c[cnt] = i;
					cnt ++;
				}
			}
			for (int i=0; i<cnt; i++) {
				a[index] = c[i];
				combination(index+1, a);
			}
			
		}
	}
	
	public static void bfs() {
		int y, x, ny, nx, time;
		while (!q.isEmpty()) {
			int[] here = q.poll();
			time = here[2];
			for (int dir=0; dir<4; dir++) {
				ny = here[0] + direct[dir][0];
				nx = here[1] + direct[dir][1];
				if (0 <= ny && ny < N && 0 <= nx && nx < N && matrix[ny][nx] == 2 && visited[ny][nx] == -1) {
					q.offer(new int[] {ny,nx,time+1});
					visited[ny][nx] = 0;
				} else if (0 <= ny && ny < N && 0 <= nx && nx < N && matrix[ny][nx] == 0 && visited[ny][nx] == -1) {
					q.offer(new int[] {ny,nx,time+1});
					visited[ny][nx] = time + 1;
				}
			}
		}
	}
	
	public static int timeCheck() {
		int max = -1;
		boolean isSuccess = true;
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
				if (visited[r][c] > max) {
					max = visited[r][c];
				} else if (visited[r][c] == -1 && matrix[r][c] == 0) {
					isSuccess = false;
					max = -1;
					break;
				}
			}
			if (!isSuccess) {
				break;
			}
		}
		return max;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		matrix = new int[N][N];
		virus = new int[10][2];
		int y, x, ans;
		int min = 987654321;
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j=0; j<N; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
				if (matrix[i][j] == 2) {
					virus[virusCount][0] = i;
					virus[virusCount][1] = j;
					virusCount ++;
				}
			}
		}
		
		comb = new int[10000][M];
		a = new int[M];
		combination(0, a);
		
		for (int i=0; i<top; i++) {
			q = new LinkedList<>();
			visited = new int[N][N];
			for (int r=0; r<N; r++) {
				for (int c=0; c<N; c++) {
					visited[r][c] = -1;
				}
			}
			for (int j=0; j<M; j++) {
				y = virus[comb[i][j]][0];
				x = virus[comb[i][j]][1];
				q.offer(new int[] {y,x,0});
			}
			bfs();
			ans = timeCheck();
			if (ans > -1 && ans < min) {
				min = ans;
			}
		}
		if (min==987654321) {
			System.out.println(-1);
		} else {
			System.out.println(min);
		}
	}

}
