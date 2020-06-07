import java.util.*;

public class Main10828_스택 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] stack = new int[10000];
		int top = -1;
		int N = sc.nextInt();
		int i,num;
		
		for (i=0; i<N; i++) {
			String s = sc.next();
			if (s.equals("push")) {
				num = sc.nextInt();
				top += 1;
				stack[top] = num;
			} else if (s.equals("pop")) {
				if (top == -1) {
					System.out.println(-1);
				} else {
					System.out.println(stack[top]);
					stack[top] = 0;
					top--;
				}
			} else if (s.equals("size")) {
				System.out.println(top+1);
			} else if (s.equals("empty")) {
				if (top == -1) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else {
				if (top == -1) {
					System.out.println(-1);
				} else {
					System.out.println(stack[top]);
				}
			}
		}
		sc.close();

	}

}