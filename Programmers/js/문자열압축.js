function solution(s) {
    var answer = 1001;
    let cArr = []
    let sArr = []
    let end = 0;
    let word = '';
    let sStr = '';
    for (let cnt=1; cnt<s.length+1; cnt++) {
        cArr = []
        sArr = []        
        for (let start=0; s.length; start+cnt) {
            end = start + end
            word = s.slice(start,end);
            cArr = cArr.concat(word);
        }

        for (let i=0; i<cArr.length; i++) {
            if (i === 0) {
                cnt++;
            } else if (cArr[i-1] === cArr[i]) {
                cnt++;
            } else {
                if (cnt !== 1) {
                    sArr = sArr.concat(String(cnt));
                }
                sArr = sArr.concat(cArr[i-1]);
                cnt++;
            }
        }
        if (cnt !== 1) {
            sArr = sArr.concat(String(cnt));
        }
        sArr = sArr.concat(cArr[cArr.length-1]);
        sStr = sArr.join();
        if (sStr.length < answer) {
            answer = sStr.length;
        } 
    }
    return answer;
}

// s	result
ex1 = "aabbaccc"	// 7
ex2 = "ababcdcdababcdcd"	// 9
ex3 = "abcabcdede"	// 8
ex4 = "abcabcabcabcdededededede"	// 14
ex5 = "xababcdcdababcdcd"	// 17
ex6 = 'a' // 1
console.log(solution(ex6))