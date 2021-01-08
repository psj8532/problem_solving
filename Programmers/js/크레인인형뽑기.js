function solution(board, moves) {
    let answer = 0;
    let arr = [];
    for (const col of moves) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][col - 1] !== 0) {
                arr.push(board[i][col - 1])
                if (arr.filter((num, i) => arr[i] === arr[i + 1]).length + 1 > 1) {
                    arr.pop();
                    arr.pop();
                    answer += 2;
                };
                board[i][col - 1] = 0;
                break;
            }
        }
    }
    return answer;
}

console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]));
// const arr = [1];
// console.log(arr.filter((num, i) => arr[i] === arr[i + 1]).length + 1);