function solution(participant, completion) {
    var answer = '';
    let pArr = participant.sort();
    let cArr = completion.sort();
    let pName = '';
    let cName = '';
    for (let i = 0; i<cArr.length; i++) {
        pName = pArr[i];
        cName = cArr[i];
        if (pName !== cName) {
            answer = pName;
            break;
        }
    }
    if (answer === '') {
        answer = pArr[pArr.length-1];
    }
    return answer;
}

// participant	completion	return
ex1 = [["leo", "kiki", "eden"], ["eden", "kiki"]]	// leo
ex2 = [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]]	// vinko
// ex3 = [[mislav, stanko, mislav, ana],[stanko, ana, mislav]]	// mislav
ex4 = [["a","aa","aaa"],["aaa","a"]]
console.log(solution(ex4[0], ex4[1]));