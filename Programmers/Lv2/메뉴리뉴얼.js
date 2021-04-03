const solution = (orders, course) => {
    let comb = [];
    let max = 0;
    const answer = [];
    const combination = (k, a, cSize, orderSize) => {
        if (k === cSize) {
            const temp = a.map(v => v);
            comb.push(temp);
            return;
        }
        const inComb = new Array(orderSize).fill(false);
        for (let i = 0; i < k; i++) {
            inComb[a[i]] = true;
        }
        let posi = 0;
        for (let i = orderSize - 1; i >= 0; i--) {
            if (inComb[i]) {
                posi = i + 1;
                break;
            }
        }
        const c = new Array(cSize).fill(0);
        let cnt = 0;
        for (let i = posi; i < orderSize; i++) {
            if (!inComb[i]) {
                c[cnt++] = i;
            }
        }
        for (let i = 0; i < cnt; i++) {
            a[k] = c[i];
            combination(k + 1, a, cSize, orderSize);
        }
    };

    course.forEach(courseCnt => {
        const foods = {};
        orders.forEach(order => {
            comb = [];
            const orderLength = order.length;
            const newOrder = [...order].sort().join('');
            if (orderLength >= courseCnt) {
                combination(0, new Array(courseCnt).fill(0), courseCnt, orderLength);
            }
            comb.forEach(c => {
                const foodComb = c.map(cVal => newOrder[cVal]).join('');
                if (foodComb in foods) {
                    foods[foodComb]++;
                } else {
                    foods[foodComb] = 1;
                }
            })
        });
        let m = [];
        max = 0;
        for (const [food, cnt] of Object.entries(foods)) {
            if (cnt > max) {
                m = [food];
                max = cnt;
            } else if (cnt === max) {
                m.push(food);
            }
        }
        if (max > 1) {
            answer.push(...m);
        }
    });

    return answer.sort();
};

// orders	course	result
const ex1 = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]];	// ["AC", "ACDE", "BCFG", "CDE"]]
const ex2 = [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]];	// ["ACD", "AD", "ADE", "CD", "XYZ"]
const ex3 = [["XYZ", "XWY", "WXA"], [2, 3, 4]];	// ["WX", "XY"]

console.log(solution(ex3[0], ex3[1]));