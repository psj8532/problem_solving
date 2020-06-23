import java.util.*;
public class Main1244_스위치켜고끄기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i, j, idx;
		int s = sc.nextInt();
		int[] data = new int[s];
		for (i=0; i<s; i++) {
			data[i] = sc.nextInt();
		}
		int n = sc.nextInt();
		int[][] stu = new int[n][2];
		for (i=0; i<n; i++) {
			stu[i][0] = sc.nextInt();
			stu[i][1] = sc.nextInt();
		}
		
		for (i=0; i<n; i++) {
			idx = stu[i][1]-1;
			if (stu[i][0] == 1) {
				for (j=idx; j<s; j+=stu[i][1]) {
					data[j] = 1-data[j];
				}
			} else {
				j = 1;
				data[idx] = 1-data[idx];
				while ((0 <= idx-j) && (idx+j < s)) {
					if (data[idx-j] == data[idx+j]) {
						data[idx-j] = 1 - data[idx-j];
						data[idx+j] = 1 - data[idx+j];
					} else {
						break;
					}
					j++;
				}
			}
		}
		
		for (i=0; i<s; i++) {
			if (i%20==19) {
				System.out.println(data[i]);
			} else {
				System.out.print(data[i]+" ");
			}
		}
		sc.close();

	}

}
