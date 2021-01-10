function solution(n) {
    return String(n).split('').reduce((acc, cur) => {
        return acc += +cur
    }, 0);
}

console.log(solution(123))