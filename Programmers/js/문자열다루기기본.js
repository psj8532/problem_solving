function solution(s) {
    function checkLength(str) {
        return (str.length === 4) || (str.length === 6);
    }

    function checkNum(num) {
        for (let i = 0; i < num.length; i++) {
            if (isNaN(num[i])) {
                return false;
            }
        }
        return true;
    }

    return checkLength(s) && checkNum(s);
}

console.log(solution("a234")); // false
console.log(solution("1234")) // true
console.log(solution("123 "));
console.log(solution("1234 5"))