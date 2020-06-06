import java.util.*;

public class Main9498_시험성적 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int grade = sc.nextInt();
		char ch;
		if (grade>=90 && grade<=100) {
			ch = 'A';
		} else if (grade>=80 && grade<=89) {
			ch = 'B';
		} else if (grade>=70 && grade<=79) {
			ch = 'C';
		} else if (grade>=60 && grade<=69) {
			ch = 'D';
		} else {
			ch = 'F';
		}
		System.out.println(ch);
		sc.close();
	}

}