import java.util.*;

public class Main4344_평균은넘겠지 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int i,sum,count;
		double avg,result;
		for (int tc=0; tc<t; tc++) {
			int n = sc.nextInt();
			int[] arr = new int[n];
			sum = 0;
			count = 0;
			for (i=0; i<n; i++) {
				arr[i] = sc.nextInt();
				sum += arr[i];
			}
			avg = sum / (double)n;
			for (i=0; i<n; i++) {
				if (arr[i]>avg) {
					count++;
				}
			}
			result = (count/(double)n)*100;
			System.out.println(String.format("%.3f", result) + '%');
		}
		sc.close();
	}

}