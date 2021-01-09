// function solution(n) {
//     let answer = 0;
//     const prime = [];
//     let target, targetIdx, isFail;
//     for (let number = 2; number <= n; number++) {
//         // console.log('현재 숫자: ' + number);
//         if (prime.length === 0) {
//             prime.push(number);
//             answer++;
//         } else {
//             target = ~~Math.sqrt(number);
//             // console.log('target: ' + target);
//             isFail = false;
//             for (let i = 0; i < prime.length; i++) {
//                 if (!isFail && prime[i] > target) {
//                     break
//                 } else if (!(number % prime[i])) {
//                     isFail = true;
//                 }
//             }
//             if (!isFail) {
//                 prime.push(number);
//                 answer++;
//             }

//         }
//         // console.log(prime);
//     }
//     return answer;
// }

function solution(n) {
    let visited = new Array(n + 1).fill(0)
    const target = ~~Math.sqrt(n);
    for (let num = 2; num <= target; num++) {
        if (visited[num]) {
            continue;
        } else {
            for (let i = num * 2; i <= n; i += num) {
                visited[i] = 1;
            }
        }
    }
    return visited.filter(function (value, idx) {
        if (idx >= 2 && visited[idx] === 0) {
            return true;
        }
    }).length;
}

console.log(solution(10)); // 4
console.log(solution(5)); // 3