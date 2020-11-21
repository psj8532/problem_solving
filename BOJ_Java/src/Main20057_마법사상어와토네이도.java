import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main20057_마법사상어와토네이도 {
	private static int N;
	private static int[][] links;
	private static boolean[][] visited;
	private static int[][] direct = {
			{0,-1},
			{1,0},
			{0,1},
			{-1,0},
	};
	private static int[][] dy = {
			{-1,1,-2,2,-1,1,-1,1,0,0}, // 10 # 1%,2%,7%,10%,5%,나머지
		    {-1,-1,0,0,0,0,1,1,2,1},
		    {-1,1,-2,2,-1,1,-1,1,0,0},
		    {1,1,0,0,0,0,-1,-1,-2,-1},
	};
	private static int[][] dx = {
			{1,1,0,0,0,0,-1,-1,-2,-1},
		    {-1,1,-2,2,-1,1,-1,1,0,0},
		    {-1,-1,0,0,0,0,1,1,2,1},
		    {-1,1,-2,2,-1,1,-1,1,0,0},
	};
	public static int move(int y, int x, int d, int ans) {
		int total = 0;
		int sand = 0;
		int ny, nx;
	    for (int dir=0; dir<9; dir++) {
	        ny = y + dy[d][dir];
	        nx = x + dx[d][dir];
	        if (dir == 0 || dir == 1) {
	        	// 1%
	            sand = (int) Math.floor(links[y][x] * 0.01);
	        } else if (dir == 2 || dir ==3) {
	        	// 2%
	            sand = (int) Math.floor(links[y][x] * 0.02);
	        } else if (dir ==4 || dir == 5) {
	        	// 7%
	            sand = (int) Math.floor(links[y][x] * 0.07);
	        } else if (dir == 6 || dir == 7) {
	        	// 10%
	            sand = (int) Math.floor(links[y][x] * 0.1);
	        } else {
	        	// 5%
	        	sand = (int) Math.floor(links[y][x] * 0.05);
	        }
	            

	        if (0 <= ny && ny < N && 0 <= nx && nx < N) {
	            links[ny][nx] += sand;
	        } else {
	            ans += sand;
	        }
	        total += sand;
	        
	    }
	    // 나머지
	    ny = y + dy[d][9];
	    nx = x + dx[d][9];
	    links[y][x] -= total;
	    if (0 <= ny && ny < N && 0 <= nx && nx < N) {
	        links[ny][nx] += links[y][x];
	    } else {
	        ans += links[y][x];
	    }
	    links[y][x] = 0;
	    
	    return ans;
	}
	public static int[] tornado(int by, int bx, int bd) {
		int nd = (bd+1) % 4;
		int ny = by+direct[nd][0];
		int nx = bx+direct[nd][1];
		int[] result = new int[4];
	    if (visited[ny][nx]) {
	        ny = by+direct[bd][0];
	        nx = bx+direct[bd][1];
	        nd = bd;
	    }
	    visited[ny][nx] = true;
		result[0] = ny;
		result[1] = nx;
		result[2] = nd;
		return result;
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		links = new int[N][N];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j=0; j<N; j++) {
				links[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int y = N / 2;
		int x = N / 2;
		int d = 3;
		int answer = 0;
		visited = new boolean[N][N];
		visited[y][x] = true;
		int[] result = new int[] {y,x,d};
		while (true) {
			result = tornado(result[0],result[1],result[2]);
		    answer = move(result[0],result[1],result[2],answer);
		    if (result[0] == 0 && result[1] == 0) {
		    	break;
		    }
		}
		System.out.println(answer);
		
	}

}
