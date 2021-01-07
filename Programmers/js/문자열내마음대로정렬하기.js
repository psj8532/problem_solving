// // 15:06 ~ 
// function solution(strings, n) {
//     const tArr = strings.sort();
//     return strings
//         .map(str => (
//             [str, str.charCodeAt(n)]
//         ))
//         .sort(function (a, b) {
//             if (a[1] === b[1]) {
//                 return tArr.indexOf(a[0]) - tArr.indexOf(b[0]);
//             } else {
//                 return a[1] - b[1];
//             }
//         })
//         .map(str => str[0])
// }

function solution(strings, n) {
    const tArr = strings.sort();
    return strings
        .sort(function (a, b) {
            if (a.charCodeAt(n) === b.charCodeAt(n)) {
                return tArr.indexOf(a) - tArr.indexOf(b);
            } else {
                return a.charCodeAt(n) - b.charCodeAt(n);
            }
        })
}

// strings	n	return
ex1 = [['sun', 'bed', 'car', 'aaa'], 1]	// [car, bed, sun]
ex2 = [['abce', 'abcd', 'cdx'], 2]	// [abcd, abce, cdx]
console.log(solution(ex1[0], ex1[1]));