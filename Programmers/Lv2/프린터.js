function solution(priorities, location) {
    let answer = 0;
    const queue = priorities.map((priority, index) => new Array(priority, index));
    let isCheck = false;
    let currDocuments;

    while (!isCheck) {
        isCheck = true;
        currDocuments = queue.shift();
        for (let i = 0; i < queue.length; i++) {
            if (queue[i][0] > currDocuments[0]) {
                queue.push(currDocuments);
                isCheck = false;
                break;
            }
        }
        if (isCheck) {
            answer++;
            if (currDocuments[1] === location) break;
        }
        isCheck = false;
    }

    return answer;
}

console.log(solution([2, 1, 3, 2], 2));
console.log(solution([1, 1, 9, 1, 1, 1], 0));
