function solution(n) {
    return +(String(n).split('').map(x => +x).sort((a, b) => b - a).join(''));
}

console.log(solution(111302));