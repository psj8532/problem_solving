// Z: 96, z: 127  
function solution(s, n) {
    let answer = ''
    const u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const d = u.toLowerCase();
    [...s].forEach(element => {
        if (element === ' ') {
            answer += ' ';
        } else if (element.charCodeAt(0) < 97) {
            answer += u[(u.indexOf(element) + n) % u.length];
        } else {
            answer += d[(d.indexOf(element) + n) % d.length];
        }
    });
    return answer;
}

console.log(solution("a", 25));