import java.util.*;
import java.io.*;

public class Main17822_원판돌리기 {
	static int N, M, T;
	static int[] direct = {
			1, -1
	};
	static int[][] matrix;
	static int[][] rotateData;
	
	public static void rotate(int idx, int dir, int count) {
		int tempPull, tempKeep, nj;
		for (int cnt=0; cnt<count; cnt++) {
			tempPull = matrix[idx][0];
			if (dir == 1) {
				nj = M;
			} else {
				nj = 0;
			}
			for (int j=0; j<M; j++) {
				nj = (nj+direct[dir]) % M;
				tempKeep = matrix[idx][nj];
				matrix[idx][nj] = tempPull;
				tempPull = tempKeep;
 			}
		}
	}
	
	public static boolean check() {
		boolean isSame = false;
		int nj;
		int[][] tempMatrix = new int[N][M];
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				nj = (j+1) % M;
				if (matrix[i][j] > 0 && (matrix[i][j] == matrix[i][nj])) {
					isSame = true;
					tempMatrix[i][j] = -1;
					tempMatrix[i][nj] = -1;
				}
			}
		}
		for (int j=0; j<M; j++) {
			for (int i=0; i<N-1; i++) {
				if (matrix[i][j] > 0 && (matrix[i][j] == matrix[i+1][j])) {
					isSame = true;
					tempMatrix[i][j] = -1;
					tempMatrix[i+1][j] = -1;
				}
			}
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				if (tempMatrix[i][j] == -1) {
					matrix[i][j] = 0;
				}
			}
		}
		if (isSame) {
			return true;
		} else {
			return false;
		}
	}
	
	public static void calculate(int cnt) {
		int sum = 0;
		double avg = 0;
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				if (matrix[i][j] > 0) {
					cnt ++;
					sum += matrix[i][j];
				}
			}
		}
		if (cnt != 0) {
			avg = (double)sum / (double)cnt;
			for (int i=0; i<N; i++) {
				for (int j=0; j<M; j++) {
					if (matrix[i][j] > 0) {
						if (matrix[i][j] > avg) {
							matrix[i][j] --;
						} else if (matrix[i][j] < avg) {
							matrix[i][j] ++;
						}
					}
				}
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int x, d, k;
		int result = 0;
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		matrix = new int[N][M];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j=0; j<M; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		rotateData = new int[T][3];
		for (int i=0; i<T; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			rotateData[i][0] = Integer.parseInt(st.nextToken());
			rotateData[i][1] = Integer.parseInt(st.nextToken());
			rotateData[i][2] = Integer.parseInt(st.nextToken());
		}

		for (int t=0; t<T; t++) {
			x = rotateData[t][0];
			d = rotateData[t][1];
			k = rotateData[t][2];
			for (int num=1; num<N+1; num++) {
				if (num % x == 0) {
					rotate(num-1, d, k);
				}
			}
			if (!check()) {
				calculate(0);
			}					
		}
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				if (matrix[i][j] > 0) {
					result += matrix[i][j];
				}
			}
		}
		System.out.println(result);

	}

}
