import java.util.*;

public class Main2753_윤년 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int year = sc.nextInt();
		int ans = 0;
		if ((year%400==0)||(year%4==0 && year%100!=0)) {
			ans = 1;
		}
		System.out.println(ans);
		sc.close();
	}

}