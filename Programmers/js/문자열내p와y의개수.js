function solution(s) {
    const pCnt = s.toLowerCase().split('').filter(ch => ch === 'p').length;
    const yCnt = s.toLowerCase().split('').filter(ch => ch === 'y').length;
    // const { p, y } = s.toLowerCase().split('').reduce((acc, curr) => {
    //     if (curr === 'p') {
    //         acc.p++;
    //     } else if (curr === 'y') {
    //         acc.y++;
    //     }
    //     return acc;
    // }, { p: 0, y: 0 });
    return pCnt === yCnt;
}

// console.log(solution("pPoooyY"));
console.log(solution("Pyy"));