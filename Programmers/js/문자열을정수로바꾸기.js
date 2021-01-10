function solution(s) {
    return s[0] === '-' ? -Number(s.slice(1)) : Number(s);
}

// 간단한 방법
// function solution(s) {
//     return +s;
// }
// string to int : +str
// int to str : ""+int