import java.util.*;

public class Main5543_상근날드 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] burger = new int[3];
		int[] beverage = new int[2];
		int diff = 50;
		int min = 987654321;
		int i,j;	
		
		for (i=0; i<3; i++) {
			burger[i] = sc.nextInt();
		}
		for (i=0; i<2; i++) {
			beverage[i] = sc.nextInt();
		}
		for (i=0; i<3; i++) {
			for (j=0; j<2; j++) {
				if (burger[i]+beverage[j]-diff < min) {
					min = burger[i]+beverage[j]-diff;
				}
			}
		}
		System.out.println(min);
		sc.close();
	}

}