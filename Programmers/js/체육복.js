function solution(n, lost, reserve) {
    const overlap = reserve.filter(num => ~lost.indexOf(num));
    let completion = [...overlap];
    let answer = lost.filter(function (num) {
        if (~overlap.indexOf(num)) {
            return true;
        }
        if (~reserve.indexOf(num - 1) && !~completion.indexOf(num - 1)) {
            completion.push(num - 1);
            return true;
        } else if (~reserve.indexOf(num + 1) && !~completion.indexOf(num + 1)) {
            completion.push(num + 1);
            return true;
        }
    }).length;

    return n - (lost.length - answer);
}


// n	lost	reserve	return
// console.log(solution(5, [2, 4], [1, 3, 5]))	// 5
// console.log(solution(5, [2, 4], [3]))	// 4
// console.log(solution(3, [3], [1]))	// 2
console.log(solution(5, [2, 3, 4], [1, 2, 5]))	// 2