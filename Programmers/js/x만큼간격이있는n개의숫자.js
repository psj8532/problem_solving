// function solution(x, n) {
//     let answer = [];
//     for (let cnt = 0, start = x; cnt < n; cnt ++) {
//         answer.push(start);
//         start += x;
//     }
//     return answer;
// }

function solution(x, n) {
    return new Array(n).fill(x).map((v, idx) => v * (idx + 1));
}