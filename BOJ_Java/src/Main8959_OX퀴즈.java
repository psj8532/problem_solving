import java.util.*;

public class Main8959_OX퀴즈 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int tc=0; tc<t; tc++) {
			String s = sc.next();
			char[] arr = new char[s.length()];
			int i;
			int cnt = 0;
			int score = 0;
			for (i=0; i<s.length(); i++) {
				arr[i] = s.charAt(i);
			}
			for (i=0; i<s.length(); i++) {
				if (arr[i] == 'O') {
					++cnt;
					score += cnt;

				} else {
					cnt = 0;
				}
			}
			System.out.println(score);
		}
		
		sc.close();
	}

}
// nextInt() 다음에 nextLine을 쓰면
// nextInt() 실행후 눌려지는 엔터가 그대로 남아있어 
// nextLine 메소드 실행시 엔터를 인식하여 바로 종료