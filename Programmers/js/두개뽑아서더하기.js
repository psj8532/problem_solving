function solution(numbers) {
    let arr = [];
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            arr.push(numbers[i] + numbers[j]);
        }
    }

    const answer = [...new Set(arr)];

    return answer.sort((a, b) => a - b);
}

// numbers	result
ex1 = [2, 1, 3, 4, 1];	// [2,3,4,5,6,7]
ex2 = [5, 0, 2, 7];	// [2,5,7,9,12]
console.log(solution(ex2));