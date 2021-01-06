// function solution(n) {
//     var answer = '';

//     let q = ~~(n / 2);
//     let r = n % 2;
//     if (q === 0) {
//         return '수';
//     }
//     for (let i = 0; i < q; i++) {
//         answer += '수박'
//     }
//     if (r === 1) {
//         answer += '수'
//     }

//     return answer;
// }

function solution(n) {
    return '수박'.repeat(~~(n / 2)) + (n % 2 === 1 ? '수' : '');
}

console.log(solution(2));