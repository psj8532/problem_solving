function solution(bridgeLength, weight, truckWeights) {
    let bridge = [];
    let currWeight = 0, time = 0;
    let leadW, leadP, move;
    let isShift = false;
    truckWeights.forEach(truck => {
        isShift = false;
        while (truck > weight - currWeight) {
            isShift = true;
            [leadW, leadP] = bridge.shift();
            move = bridgeLength - leadP + 1;
            bridge = bridge.map(([cT, cP]) => [cT, cP + move]);
            currWeight -= leadW;
            time += move;
        }
        if (isShift) {
            bridge.push([truck, 1]);
        } else {
            bridge.push([truck, 0]);
            bridge = bridge.map(([cT, cP]) => [cT, cP + 1]);
            if (bridge[0][1] > bridgeLength) {
                [leadW, leadP] = bridge.shift();
                currWeight -= leadW;
            }

            time++;
        }
        currWeight += truck;
    });

    time += bridgeLength - bridge[bridge.length - 1][1] + 1;

    return time;
}

console.log(solution(2, 10, [7, 4, 5, 6]));
console.log(solution(100, 100, [10]));
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));
console.log(solution(10, 10, [10, 10, 10, 10]));
console.log(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))
