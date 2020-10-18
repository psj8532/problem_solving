import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main4963_섬의개수_스택 {
	private static int w,h;
	private static int[][] arr;
	private static int answer = 0;
	private static boolean[][] visited;
	private static Stack<int[] > stack;
	private static int[][] direct = {
			{-1,0},
			{-1,1},
			{0,1},
			{1,1},
			{1,0},
			{1,-1},
			{0,-1},
			{-1,-1},
	};
	
	public static void dfs(int y,int x) {
		int ny,nx;
		stack = new Stack<int[]>();
		stack.push(new int[] {y,x});
		while(!stack.isEmpty()) {
			int[] here = stack.pop();
			y = here[0];
			x = here[1];
			if (!visited[y][x]) {
				visited[y][x] = true;
				for (int dir=7; dir > -1; dir--) {
					ny = y + direct[dir][0];
					nx = x + direct[dir][1];
					if (0 <= ny && ny < h && 0 <= nx && nx < w && !visited[ny][nx] && arr[ny][nx] == 1) {
						stack.push(new int[] {ny,nx});
					}
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			if (w == 0 && h == 0 ) {
				break;
			}
			answer = 0;
			arr = new int[h][w];
			visited = new boolean[h][w];
			for (int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j=0; j<w; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					if (!visited[i][j] && arr[i][j]==1) {
						dfs(i,j);
						answer++;
					}
				}
			}
			System.out.println(answer);
		}
	}
}
