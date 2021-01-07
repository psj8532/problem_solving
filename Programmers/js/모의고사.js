function solution(answers) {
    const answer = [1, 2, 3];
    let counter = [0, 0, 0];
    let people = [
        new Array(answers.length).fill(0).map((val, idx) => (idx % 5) + 1),
        [..."21232425".repeat(~~(answers.length / 8)).concat("21232425".slice(0, answers.length % 8))].map(ch => Number(ch)),
        [..."3311224455".repeat(~~(answers.length / 10)).concat("3311224455".slice(0, answers.length % 10))].map(ch => Number(ch)),
    ]
    let result = counter.map(function (num, idx) {
        let cnt = 0;
        for (let i = 0; i < answers.length; i++) {
            if (answers[i] === people[idx][i]) {
                cnt++;
            }
        }
        return cnt;
    });

    const maxVal = result.reduce(function (prev, curr) {
        return prev >= curr ? prev : curr;
    }, 0);

    return answer.filter((num, idx) => result[idx] === maxVal);
}


// function solution(answers) {
//     const answer = [1, 2, 3];

//     const peoples = [
//         [1, 2, 3, 4, 5],
//         [2, 1, 2, 3, 2, 4, 2, 5],
//         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
//     ];

//     const scores = peoples.map(people => {
//         return answers.filter((ans, idx) => people[idx % people.length] === ans).length
//     });

//     return scores.reduce((arr, curr, idx) => (
//         curr === Math.max(...scores) ? [...arr, idx + 1] : arr
//     ), []);
// }


// answers	return
ex1 = [1, 2, 3, 4, 5]	// [1]
ex2 = [1, 3, 2, 4, 2]	// [1,2,3]
ex3 = [3]
ex4 = [3, 3, 3, 4]
ex5 = [2, 1, 2, 3, 2, 4, 2, 5]
ex = [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
console.log(solution(ex5));