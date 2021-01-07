function solution(n) {
    function ternary(num) {
        const temp = [];
        let tnum = num;
        while (tnum > 1) {
            temp.push(tnum % 3);
            tnum = ~~(tnum / 3);
        }
        if (tnum === 1) {
            temp.push(tnum);
        }
        return temp;
    }

    // function decimal(arr) {
    //     let result = 0;
    //     for (let i = arr.length - 1; i > -1; i--) {
    //         if (arr[i] > 0) {
    //             result += arr[i] * Math.pow(3, arr.length - 1 - i);
    //         }
    //     }
    //     return result;
    // }
    const answer = ternary(n);
    return answer.reduce((prev, curr, idx) => (
        prev + curr * Math.pow(3, answer.length - 1 - idx)
    ), 0)

    // return decimal(ternary(n));
}

// n	result
ex1 = 45;	// 7
ex2 = 125;	// 229
console.log(solution(ex1));