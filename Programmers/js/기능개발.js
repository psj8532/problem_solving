function solution(progresses, speeds) {
    const remains = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
    const answer = [];
    let count = 0;
    let max = remains[0];
    remains.forEach((remain, index) => {
        if (remain > max) {
            max = remain
            answer.push(count);
            count = 1
        } else {
            count++;
        }
        if (index === remains.length - 1) answer.push(count);
    });
    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
console.log(solution([1], [1]));
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))