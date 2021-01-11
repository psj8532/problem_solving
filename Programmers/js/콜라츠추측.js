function solution(num) {
    let cnt = 0;
    while (cnt < 500 && num !== 1) {
        num = num % 2 ? num * 3 + 1 : num / 2;
        cnt++;
    }
    return num === 1 ? cnt : -1;
}