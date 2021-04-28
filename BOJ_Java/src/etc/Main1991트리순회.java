package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main1991트리순회 {
	
	private static Map<String, Node> nodeMap = new HashMap<String, Node>();
	
	private static class Node {
		private String data = null;
		private String left = null;
		private String right = null;
		
		public Node(String data, String left, String right) {
			this.data = data;
			this.left = this.checkData(left);
			this.right = this.checkData(right);
		}
		
		public String checkData(String data) {
			if (data.equals(".")){
				return null;
			} else {
				return data;
			}
		}
		
		public String toString() {
			return data;
		}
	}
	
	private static class Tree {
		private static Node root;
		
		public Tree(Node node) {
			this.root = node;
		}
		
		public void preorder(Node node) {
			System.out.print(node.toString());
			if (node.left != null) {
				this.preorder(nodeMap.get(node.left));
			}
			if (node.right != null) {
				this.preorder(nodeMap.get(node.right));
			}
		}
		
		public void inorder(Node node) {
			if (node.left != null) {
				this.inorder(nodeMap.get(node.left));
			}
			System.out.print(node.toString());
			if (node.right != null) {
				this.inorder(nodeMap.get(node.right));
			}
		}
		
		public void postorder(Node node) {
			if (node.left != null) {
				this.postorder(nodeMap.get(node.left));
			}
			if(node.right != null) {
				this.postorder(nodeMap.get(node.right));
			}
			System.out.print(node.toString());
		}
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			String data = st.nextToken();
			String left = st.nextToken();
			String right = st.nextToken();
			Node node = new Node(data, left, right);
			nodeMap.put(data, node);
		}
		Tree tree = new Tree(nodeMap.get("A"));
		tree.preorder(tree.root);
		System.out.println();
		tree.inorder(tree.root);
		System.out.println();
		tree.postorder(tree.root);
		
	}

}
