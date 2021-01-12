function solution(n) {
    let answer = 0;
    let dp = new Array(100001).fill(0)
    dp[1] = 1;
    for (let i = 2; i <= n; i++) {
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567;
    }
    return dp[n];
}
console.log(solution(100000))