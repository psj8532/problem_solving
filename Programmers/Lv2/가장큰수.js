function solution(numbers) {
    const answer = numbers
        .map(number => {
            const strNum = number + '';
            const repNum = strNum.repeat(4).slice(0, 4);
            return [strNum, repNum];

        })
        .sort((a, b) => {
            const aNum = a[1] * 1;
            const bNum = b[1] * 1;
            return bNum - aNum;
        })
        .map(nums => nums[0])
        .join('');
    return parseInt(answer) === 0 ? '0' : answer;
}

console.log(solution([6, 10, 2]));
console.log(solution([3, 30, 34, 5, 9]));
console.log(solution([0, 0]));
console.log(solution([12, 124]))