package programmers;

public class Main자물쇠와열쇠 {
	
	private static int paddingSize, keySize, lockSize, matrixSize;
	
	private static int[][] copy(int[][] original) {
		int[][] newArr = new int[keySize][keySize];
		for (int i = 0; i < keySize; i++) {
			for (int j = 0; j < keySize; j++) {
				newArr[i][j] = original[i][j];
			}
		}
		return newArr;
	}
	
	private static int[][] rotate(int[][] original) {
		int[][] newArr = new int[keySize][keySize];
		for (int i = 0; i < keySize; i++) {
			for (int j = 0; j < keySize; j++) {
				newArr[j][keySize - 1 - i] = original[i][j];
			}
		}
		return newArr;
	}
	
	private static boolean check(int ky, int kx, int[][] key, int[][] lock) {
		int[][] matrix = new int[matrixSize][matrixSize];
		
		for (int i = 0; i < keySize; i++) {
			for (int j = 0; j < keySize; j++) {
				int keyVal = key[i][j];
				matrix[ky + i][kx + j] += keyVal;
			}
		}
		
		for (int i = 0; i < lockSize; i++) {
			for (int j = 0; j < lockSize; j++) {
				int lockVal = lock[i][j];
				if (matrix[paddingSize + i][paddingSize + j] + lockVal != 1) return false;
			}
		}
		
		return true;
		
	}
	
	private static boolean solution(int[][] key, int[][] lock) {
        keySize = key.length; 
        lockSize = lock.length;
        int[][] newKey = copy(key);
        paddingSize = keySize - 1;
        matrixSize = 2 * paddingSize + lockSize;
        int rotation = 0;
        
        while (rotation < 4) {
        	for (int ki = 0; ki < matrixSize - paddingSize; ki++) {
        		for (int kj = 0; kj < matrixSize - paddingSize; kj++) {
        			if (check(ki, kj, newKey, lock)) return true;
        		}
        	}
        	
        	newKey = rotate(newKey);
			rotation++;
        }
        
        return false;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// key	lock	result
		int[][] k = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};	
		int[][] l = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
		
		System.out.println(solution(k, l));

	}

}
