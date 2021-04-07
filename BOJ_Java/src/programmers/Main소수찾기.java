package programmers;

import java.util.*;

public class Main소수찾기 {
	
	private static List<int[]> perm = new ArrayList<>();
	
	private static Set<Integer> primes = new HashSet<>();
	
	private static int[] copy(int[] original) {
		int[] newArr = new int[original.length];
		for (int i = 0; i < original.length; i++) newArr[i] = original[i];
		return newArr;
	}
	
	private static void permutation(int k, int[] a, int pSize, int totalSize) {
		if (k == pSize) {
			int[] temp = copy(a);
			perm.add(temp);
			return;
		}
		
		boolean[] inPerm = new boolean[totalSize];
		for (int i = 0; i < k; i++) inPerm[a[i]] = true;
		
		int[] c = new int[totalSize];
		int cnt = 0;
		for (int i = 0; i < totalSize; i++) {
			if (inPerm[i]) continue;
			c[cnt++] = i;
		}
		
		for (int i = 0; i < cnt; i++) {
			a[k] = c[i];
			permutation(k+1, a, pSize, totalSize);
		}
	}
	
	private static boolean checkPrime(int num) {
		if (num <= 1) return false;
		for (int i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
			if (num % i == 0) return false;
		}
		return true;
	}
	
	private static int solution(String numbers) {
        int numbersSize = numbers.length();
        
        for (int permSize = 1; permSize <= numbersSize; permSize++) {
        	int[] a = new int[permSize];
        	permutation(0, a, permSize, numbersSize);
        }
        
        for (int[] p : perm) {
        	String strNum = "";
        	for (int pVal : p) {
        		strNum += numbers.charAt(pVal);
        	}
        	int num = Integer.parseInt(strNum);
        	if (checkPrime(num) && !primes.contains(num)) {
        		primes.add(num);
        	}
        }
        
        return primes.size();
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(solution("17"));
	}

}
