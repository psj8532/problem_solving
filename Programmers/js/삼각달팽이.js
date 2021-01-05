function solution(n) {
    var answer = [];
    const dy = [1,0,-1];
    const dx = [0,1,-1];
    let triangle = new Array(n);
    for (let i=0; i < n; i++) {
        triangle[i] = new Array(i+1);
    }
    const end = n * (n+1) / 2;
    let num = 0, dir = 0;

    let y = -1, x = 0;
    let ny = y, nx = x;
    while (num < end) {
        ny = y + dy[dir];
        nx = x + dx[dir];
        if (ny < 0 || ny >= n || nx < 0 || nx >= n || triangle[ny][nx] !== undefined) {
            dir++;
            dir %= 3;
            ny = y + dy[dir];
            nx = x + dx[dir];
        }
        num ++;
        triangle[ny][nx] = num;
        y = ny;
        x = nx;
    }
    for (let i=0; i<n; i++) {
        answer = answer.concat(triangle[i]);
    }

    return answer;
}

ex1 = 4	// [1,2,9,3,10,8,4,5,6,7]
ex2 = 5	// [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
ex3 = 6	// [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
console.log(solution(ex3))