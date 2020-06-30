import java.io.*;
import java.util.*;

public class Main17406_배열돌리기4 {
	static int N, M, K;
	static int[][] matrix;
	static int[][] tempMatrix;
	static int[][] rotation;
	static int[][] direct = {
			{0,1},
			{1,0},
			{0,-1},
			{-1,0},
	};
	static boolean[][] visited;
//	static int[][] perm;
	static int[] a;
	static int top = 0;
	static int min = 987654321;
	static Queue<int[] > q = new LinkedList<>();
	
	public static void permutation(int index, int[] a) {
		int i,j,cnt;
		if (index == K) {
			int[] temp = new int[K];
			for (i=0; i<K; i++) {
				temp[i] = a[i];
			}
			q.offer(temp);
//			for (i=0; i<K; i++) {
//				q[top][i] = a[i];
//			}
			top ++;
		} else {
			boolean[] inPerm = new boolean[K];
			for (i=0; i<index; i++) {
				inPerm[a[i]] = true;
			}
			int[] c = new int[K];
			cnt = 0;
			for (i=0; i<K; i++) {
				if (!inPerm[i]) {
					c[cnt] = i;
					cnt ++;
				}
			}
			for (i=0; i<cnt; i++) {
				a[index] = c[i];
				permutation(index+1, a);
			}
		}
	}
	
	public static int[][] copy(int[][] o, int[][] n) {
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				n[i][j] = o[i][j];
			}
		}
		return n;
	}
	
	public static void count() {
		int sum;
		for (int i=0; i<N; i++) {
			sum = 0;
			for (int j=0; j<M; j++) {
				sum += matrix[i][j];
				if (sum > min) {
					break;
				}
			}
			if (sum < min) {
				min = sum;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		int i,j,r,c,s;
		int dir,y,x,ny,nx;
		int temp1,temp2;
		matrix = new int[N][M];
		tempMatrix = new int[N][M];
		
		for (i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (j=0; j<M; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		rotation = new int[K][3];
		for (i=0; i<K; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (j=0; j<3; j++) {
				rotation[i][j] = Integer.parseInt(st.nextToken());	
			}
		}
		
		a = new int[K];
//		perm = new int[720][K];
		permutation(0, a);
		
		tempMatrix = copy(matrix,tempMatrix);
//		for (i=0; i<top; i++) {
		while (!q.isEmpty()) {
			int[] perm =  q.poll();
//			for (i=0; i<K; i++) {
//				System.out.print(perm[i] + " ");
//			}
//			System.out.println();
			for (j=0; j<K; j++) {
				visited = new boolean[N][M];
				r = rotation[perm[j]][0]-1;
				c = rotation[perm[j]][1]-1;
				s = rotation[perm[j]][2];
				for (int idx=1; idx<=s; idx++) {
					dir = 0;
					y = r - idx;
					x = c - idx;
					ny = y + direct[dir][0];
					nx = x + direct[dir][1];
					temp1 = matrix[y][x];
					while (!visited[ny][nx]) {
						temp2 = matrix[ny][nx];
						matrix[ny][nx] = temp1;
						temp1 = temp2;
						y = ny;
						x = nx;
						visited[y][x] = true;
						if ((y==r-idx && x==c-idx) || (y==r-idx && x==c+idx) || (y==r+idx && x==c-idx) || (y==r+idx && x==c+idx)) {
							dir = (dir+1) % 4;
						}
						ny = y + direct[dir][0];
						nx = x + direct[dir][1];
					}
				}
//				for (int q=0; q<N; q++) {
//					for (int w=0; w<M; w++) {
//						System.out.print(matrix[q][w] + " ");
//					}
//					System.out.println();
//				}
//				System.out.println();
			}
			count();			
			matrix = copy(tempMatrix, matrix);
		}
		System.out.println(min);
	}

}
