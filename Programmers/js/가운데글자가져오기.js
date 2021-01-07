function solution(s) {
    // let answer = '';
    // function odd(target) {
    //     return s.slice(target, target + 1);
    // }

    // function even(target) {
    //     return s.slice(target, target + 2);
    // }

    // if (s.length % 2) {
    //     answer = odd(~~(s.length / 2));
    // } else {
    //     answer = even(s.length / 2 - 1);
    // }

    const mid = ~~(s.length / 2);
    return s.length % 2 ? s.slice(mid, mid + 1) : s.slice(mid - 1, mid + 1);
}

// s	return
ex1 = "abcde";	// c
ex2 = "qwer";	// we
console.log(solution(ex1));