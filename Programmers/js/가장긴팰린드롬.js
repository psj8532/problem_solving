function solution(s) {
    let answer = 0, N = s.length;
    let left, right, mid;
    for (let cnt = 2; cnt <= N; cnt++) {
        for (let i = 0; i <= N - cnt; i++) {
            mid = ~~(cnt / 2);
            left = s.slice(i, i + mid);
            if (cnt % 2) {
                right = s.slice(i + mid + 1, i + mid + 1 + mid);
            } else {
                right = s.slice(i + mid, i + mid + mid);
            }
            right = [...right].reverse().join('');
            if (left === right) {
                answer = cnt;
                break;
            }
        }
    }

    return answer;
}

console.log(solution('abcdcba'))