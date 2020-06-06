import java.util.*;

public class Main2588_곱셈 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a,b;
		int[] result = new int[4];
		int temp,num;
		int i = 0;
		a = sc.nextInt();
		b = sc.nextInt();
		temp = b;
		while (temp != 0) {
			num = temp % 10;
			result[i] = a * num;
			temp /= 10;
			i++;
		}
		result[3] = a * b;
		for (int j=0; j<result.length; j++) {
			System.out.println(result[j]);
		}
	}

}