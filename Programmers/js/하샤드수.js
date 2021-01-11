function solution(x) {
    const answer = x + ''.split('').map(v => +v).reduce((acc, cur) => (acc + cur), 0);
    return !(x % answer);
}