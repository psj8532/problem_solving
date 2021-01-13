function solution(s) {
    return s.split(" ")
        .map((word) => {
            let ch = word.charAt(0);
            let c = isNaN(ch) ? ch.toUpperCase() : ch;
            return c + word.slice(1, word.length).toLowerCase();
        })
        .join(' ');
}

console.log(solution("3people unFollowed me"));