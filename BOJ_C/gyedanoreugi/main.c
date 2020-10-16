/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int N;
int arr[300];
int dp[300][2];

int max(int a, int b);

int main()
{
    int answer = 0;
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d", &arr[i]);
    }
    dp[0][0] = arr[0];
    if (N > 1) {
        dp[1][0] = arr[1];
        dp[1][1] = dp[0][0] + arr[1];
        for (int i=2; i<N; i++) {
            dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + arr[i];
            dp[i][1] = dp[i-1][0] + arr[i];
        }
        answer = max(dp[N-1][0],dp[N-1][1]);
    } else {
        answer = arr[0];
    }
    printf("%d\n", answer);

    return 0;
}

int max(int a, int b) {
    return a >= b ? a : b;
}
