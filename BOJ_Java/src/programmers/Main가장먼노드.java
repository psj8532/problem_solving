package programmers;

import java.util.*;

public class Main가장먼노드 {
	
	private static int[] answer = new int[20000];
	private static Map<Integer, ArrayList<Integer>> adj = new HashMap<Integer, ArrayList<Integer>>();
	
	private int bfs(int start, int depth, int n) {
		int d = depth;
		List<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] {start, depth});
		boolean[] visited = new boolean[n+1];
		visited[start] = true;
		
		while (!queue.isEmpty()) {
			int[] hereData = queue.remove(0);
			int here = hereData[0];
			d = hereData[1];
			answer[d]++;
			for (int next : adj.get(here)) {
				if (!visited[next]) {
					queue.add(new int[] {next, d+1});
					visited[next] = true;
				}
			}
		}
		
		return d;
	}
	
	private int solution(int n, int[][] edge) {
		for (int i = 1; i <= n; i++) {
			adj.put(i, new ArrayList<Integer>());
		}
		
        for (int[] route : edge) {
        	int start = route[0], end = route[1];
        	ArrayList<Integer> original = adj.get(start);
        	original.add(end);
        	adj.put(start, original);
        	
        	original = adj.get(end);
        	original.add(start);
        	adj.put(end, original);
        }
        
        int rear = bfs(1, 0, n);
		
        return answer[rear];
    }

}
