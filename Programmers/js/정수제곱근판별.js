function solution(n) {
    let answer = Math.sqrt(n);
    return answer % 1 ? -1 : Math.pow(answer + 1, 2);
}