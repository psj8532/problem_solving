function solution(s) {
    return s.split(' ').map(function (word) {
        let words = ''
        for (let i = 0; i < word.length; i++) {
            if (i % 2) {
                words += word[i].toLowerCase();
            } else {
                words += word[i].toUpperCase();
            }
        }
        return words
    }).join(' ')
}