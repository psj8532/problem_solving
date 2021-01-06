// function solution(arr) {
//     var answer = [];
//     let prev = arr[0];
//     for (let i = 1; i < arr.length; i++) {
//         if (arr[i] !== prev) {
//             answer.push(prev);
//             prev = arr[i];
//         }
//     }
//     answer.push(prev);

//     return answer;
// }

function solution(arr) {
    return arr.filter((val, idx) => val !== arr[idx + 1]);
}

// function solution(arr) {
//     var answer = [];
//     let prev = arr[0];
//     for (let i = 1; i < arr.length; i++) {
//         if (arr[i] !== prev) {
//             answer = [...answer, prev];
//             prev = arr[i];
//         }
//     }
//     answer = [...answer, prev];

//     return answer;
// }

// arr	answer
ex1 = [1, 1, 3, 3, 0, 1, 1] // [1,3,0,1]
ex2 = [4, 4, 4, 3, 3] // [4,3]
console.log(solution(ex2));