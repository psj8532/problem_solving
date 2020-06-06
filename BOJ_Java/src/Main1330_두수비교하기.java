import java.util.*;

public class Main1330_두수비교하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A,B;
		String result;
		A = sc.nextInt();
		B = sc.nextInt();
		if (A>B) {
			result = ">";
		} else if (A<B) {
			result = "<";
		} else {
			result = "==";
		}
		System.out.println(result);
		sc.close();
	}

}