/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int N;
int arr[10000];
int dp[10000][3];

int max(int a, int b);

int main(void) {
	int answer, answer1, answer2 = 0;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	dp[0][0] = arr[0];
	if (N > 1) {
		dp[1][0] = arr[1];
		dp[1][1] = dp[0][0] + arr[1];
		for (int i = 2; i < N; i++) {
			dp[i][0] = max(dp[i - 2][0], max(dp[i - 2][1], dp[i - 2][2])) + arr[i];
			dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + arr[i];
			if (i > 2) {
				dp[i][2] = max(dp[i - 3][0], max(dp[i - 3][1], dp[i - 3][2])) + arr[i];
			}
		}
		answer1 = max(dp[N - 2][0], max(dp[N - 2][1], dp[N - 2][2]));
		answer2 = max(dp[N - 1][0], max(dp[N - 1][1], dp[N - 1][2]));
		answer = max(answer1, answer2);
	}
	else {
		answer = arr[0];
	}
	printf("%d\n", answer);
	return 0;
}

int max(int a, int b) {
	return a >= b ? a : b;
}