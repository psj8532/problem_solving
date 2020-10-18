import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main4963_섬의개수 {
	private static int w,h;
	private static int[][] arr;
	private static int answer = 0;
	private static boolean[][] visited;
	private static Queue<int[] > q;
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
	
	public static void bfs(int y,int x) {
		int ny,nx;
		q = new LinkedList<>();
		q.offer(new int[] {y,x});
		visited[y][x] = true;
		while(!q.isEmpty()) {
			int[] here = q.poll();
			y = here[0];
			x = here[1];
			for (int dir=0; dir<8; dir++) {
				ny = y + direct[dir][0];
				nx = x + direct[dir][1];
				if (0 <= ny && ny < h && 0 <= nx && nx < w && !visited[ny][nx] && arr[ny][nx] == 1) {
					q.offer(new int[] {ny,nx});
					visited[ny][nx] = true;
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
						bfs(i,j);
						answer++;
					}
				}
			}
			System.out.println(answer);
		}
	}

}
