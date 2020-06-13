import java.util.*;

public class Main10871_X보다작은수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i;
		int N = sc.nextInt();
		int X = sc.nextInt();
		int[] A = new int[N];
		
		for (i=0; i<N; i++) {
			A[i] = sc.nextInt();
			if (A[i]<X) {
				System.out.print(A[i]+ " ");
			}
		}
		sc.close();
	}

}
