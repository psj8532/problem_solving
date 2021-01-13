function solution(arr1, arr2) {
    let answer = new Array(arr1.length);
    for (let i = 0; i < arr1.length; i++) {
        answer[i] = new Array(arr2[0].length).fill(0);
    }
    for (let i = 0; i < answer.length; i++) {
        for (let j = 0; j < answer[0].length; j++) {
            for (let idx = 0; idx < arr1[0].length; idx++) {
                answer[i][j] += arr1[i][idx] * arr2[idx][j];
            }
        }
    }
    return answer;
}

// arr1	arr2	return
console.log(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))	// [[15, 15], [15, 15], [15, 15]]
console.log(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))	// [[22, 22, 11], [36, 28, 18], [29, 20, 14]]