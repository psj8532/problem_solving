function solution(d, budget) {
    const arr = d.sort((a, b) => a - b);
    let cnt = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] <= budget) {
            budget -= arr[i];
            cnt++;
        } else {
            break;
        }
    }
    return cnt
}