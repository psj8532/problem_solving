import java.util.*;

public class Main2884_알람시계 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if (m-45 >= 0) {
			m -= 45;
		} else {
			m = 60 + (m-45);
			if (h-1 >= 0) {
				h -= 1;
			} else {
				h = 24 + (h-1);
			}
		}
		System.out.print(h+" ");
		System.out.print(m);
		sc.close();
	}

}