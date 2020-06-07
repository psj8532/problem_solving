import java.util.*;

public class Main10817_세수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[3];
		for (int i=0; i<3; i++) {
			arr[i] = sc.nextInt();
		}
		int min = arr[0];
		int max = arr[0];
		int mid = arr[0];
		for (int i=1; i<3; i++) {
			if (arr[i]>max) {
				mid = max;
				max = arr[i];
			} else if (arr[i]<min) {
				mid = min;
				min = arr[i];
			} else {
				mid = arr[i];
			}
		}
		System.out.println(mid);
		sc.close();
	}

}