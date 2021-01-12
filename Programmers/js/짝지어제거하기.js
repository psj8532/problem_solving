function solution(s) {
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if (!stack || stack[stack.length - 1] !== s[i]) {
            stack.push(s[i]);
        } else if (stack && stack[stack.length - 1] === s[i]) {
            stack.pop();
        }
    }

    return stack.length ? 0 : 1;
}

// s	result
// console.log(solution("baabaa"));	// 1
// console.log(solution("cdcd"));	// 0
// console.log(solution("d"));	// 0

// console.log(solution("addd"));	// 0
// console.log(solution("add"));	// 0
// console.log(solution("baaa"));  // 0
// console.log(solution("baab"));  // 1

// console.log(solution("cabac"));