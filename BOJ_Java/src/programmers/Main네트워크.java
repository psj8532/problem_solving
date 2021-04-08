package programmers;

import java.util.Stack;

public class Main네트워크 {
	
	private static boolean[] visited;
	
	private static void dfs(int start, int n, int[][] computers) {
		Stack<Integer> stack = new Stack<>();
		stack.add(start);
		
		while (stack.size() > 0) {
			int here = stack.pop();
			
			if (!visited[here]) {
				visited[here] = true;
				for (int next = n - 1; next >= 0; next--) {
					if (!visited[next] && computers[here][next] == 1) {
						stack.add(next);
					}
				}
			}
			
		}
		
	}
	
	private static int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
        	if (!visited[i]) {
        		System.out.println(i);
        		dfs(i, n, computers);
        		answer++;
        	}
        }
        
        return answer;
    }

}
