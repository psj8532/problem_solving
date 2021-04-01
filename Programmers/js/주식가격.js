function solution(prices) {
    const pricesSize = prices.length;
    const answer = prices.map((_, idx) => pricesSize - idx - 1);
    const remain = [];
    const remainIdx = [];

    const upperBound = (left, right, key) => {
        if (left >= right) {
            return right;
        }
        const middle = ~~((left + right) / 2);
        if (remain[middle] <= key) {
            return upperBound(middle + 1, right, key);
        } else {
            return upperBound(left, middle);
        }
    };

    prices.forEach((price, curr) => {
        const remainSize = remain.length;
        if (remainSize > 0 && remain[remainSize - 1] > price) {
            const targetIdx = upperBound(0, remainSize - 1, price);
            for (let prev = remainSize - 1; prev >= targetIdx; prev--) {
                answer[remainIdx[prev]] = curr - remainIdx[prev];
                remain.pop();
                remainIdx.pop();
            }
        }
        remain.push(price);
        remainIdx.push(curr);
    });

    return answer;
}

console.log(solution([1, 2, 3, 2, 3]));
console.log(solution([5, 4, 3, 2, 1]));
console.log(solution([3, 5, 6, 6, 5, 1]));