package programmers;

import java.util.*;

public class Main주식가격 {
	
	private static List<Integer> cand = new ArrayList<>();
	private static List<Integer> candDate = new ArrayList<>();
	
	private static int upperBound(int left, int right, int key) {
		if (left >= right) {
			return right;
		}
		int mid = (left + right) / 2;
		
		if (cand.get(mid) > key) {
			return upperBound(left, mid, key);
		} else {
			return upperBound(mid+1, right, key);
		}
	}
	
	private static int[] solution(int[] prices) {
        int totalDate = prices.length;
		int[] answer = new int[totalDate];
        int currDate = 0;
        
        for (int curr = 0; curr < totalDate; curr++) {
        	answer[curr] = totalDate - 1 - curr;
        }
        
        for (int priceIndex = 0; priceIndex < totalDate; priceIndex++) {
        	int price = prices[priceIndex];
        	
        	int candSize = cand.size();
        	if (cand.size() > 0 && price < cand.get(candSize-1)) {
        		int target = upperBound(0, candSize, price);
        		for (int i = candSize-1; i >= target; i--) {
        			int dPrice = cand.remove(i);
        			int dDate = candDate.remove(i);
        			answer[dDate] = priceIndex - dDate;
        		}
        	}
        	cand.add(price);
        	candDate.add(priceIndex);
        }
        
        
        return answer;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(solution(new int[] {1, 2, 3, 2, 3}));
	}
}
