const solution = (citations) => {
    let hIndex = 0;
    const newCitations = citations.sort((a, b) => b - a);
    for (let index = 0; index < newCitations.length; index++) {
        if (newCitations[index] > index) {
            hIndex = index + 1;
        } else {
            break;
        }
    }
    return hIndex;
};

// citations	return
const ex1 = [3, 0, 6, 1, 5]	// 3
const ex2 = [25, 8, 5, 3, 3] // 3
const ex3 = [10, 8, 5, 4, 3] // 4
console.log(solution(ex2));
console.log(solution(ex3));