// 14:47 ~ 15:05
function solution(arr, divisor) {
    // let answer = arr.filter(v => v % divisor === 0).sort((a, b) => a - b);
    // if (answer.length === 0) {
    //     answer = [-1];
    // }
    let answer = arr.filter(v => v % divisor === 0).sort((a, b) => a - b);
    return answer.length !== 0 ? answer : [-1];
}

ex1 = [[5, 9, 7, 10], 5];    // [5, 10]
console.log(solution(ex1[0], ex1[1]));