/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int N;
int arr[1000][3];
int dp[1000][3];

int min(int a, int b);

int main()
{
    int answer = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);
    }
    dp[0][0] = arr[0][0];
    dp[0][1] = arr[0][1];
    dp[0][2] = arr[0][2];
    for (int i = 1; i < N; i++) {
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + arr[i][0];
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i][1];
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + arr[i][2];
    }
    answer = min(dp[N-1][0],min(dp[N-1][1],dp[N-1][2]));

    printf("%d\n", answer);

    return 0;
}

int min(int a, int b) {
    return a <= b ? a : b;
}