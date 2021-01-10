// function solution(a, b) {
//     let answer = 0;
//     for (let i = 0; i < a.length; i++) {
//         answer += a[i] * b[i];
//     }
//     return answer;
// }
// map에서는 외부의 다른 배열을 참조할 수 없다.

function solution(a, b) {
    return a.reduce((acc, x, idx) => (acc += x * b[idx]), 0);
}

console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));