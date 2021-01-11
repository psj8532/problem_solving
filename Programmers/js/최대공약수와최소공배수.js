function solution(n, m) {
    let answer = [];
    let a = n >= m ? n : m;
    let b = n < m ? n : m;
    let r = 100;
    while (r) {
        r = a % b;
        a = b;
        b = r;
    }
    answer.push(a);
    answer.push(n * m / answer[0]);

    return answer;
}