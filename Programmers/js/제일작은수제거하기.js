function solution(arr) {
    const min = arr.reduce((res, cur) => (
        cur < res ? cur : res
    ), 9876543210);
    const answer = arr.slice(0, arr.indexOf(min)).concat(arr.slice(arr.indexOf(min) + 1));
    return answer.length ? answer : [-1];
}

console.log(solution([10]));