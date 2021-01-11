function solution(arr1, arr2) {
    let answer = new Array(arr1.length);
    for (let i = 0; i < arr1.length; i++) {
        answer[i] = new Array(arr1[i].length);
    }
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            answer[i][j] = arr1[i][j] + arr2[i][j];
        }
    }
    return answer;
}

// function solution(arr1, arr2) {
//     return arr1.map((r, i) => r.map((c, j) => c + arr2[i][j]));
// }

// map을 2번 쓰는 것보다 2차원 배열을 선언해서 2차원 배열을 돌면서 값을 바꾸는게 더 빠름 