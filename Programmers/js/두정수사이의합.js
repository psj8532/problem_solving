function solution(a, b) {
    var answer = 0;
    let minV, maxV, ta, tb;
    if (a === b) {
        return a;
    } else if (a * b < 0) {
        ta = Math.abs(a);
        tb = Math.abs(b);
        minV = Math.min(a, b);
        if (ta === tb) {
            return 0;
        } else if (a === minV && ta < tb) {
            for (let i = ta + 1; i <= b; i++) {
                answer += i;
            }
        } else if (a === minV && ta > tb) {
            for (let i = a; i < -tb; i++) {
                answer += i;
            }
        } else if (b === minV && ta < tb) {
            for (let i = b; i < -a; i++) {
                answer += i;
            }
        } else {
            for (let i = tb + 1; i <= a; i++) {
                answer += i;
            }
        }
    } else if (a * b > 0) {
        if (a > b) {
            for (let i = b; i <= a; i++) {
                answer += i;
            }
        } else {
            for (let i = a; i <= b; i++) {
                answer += i;
            }
        }
    } else {
        if (((a === 0) && (a > b)) || ((b === 0) && (a > b))) {
            for (let i = b; i <= a; i++) {
                answer += i;
            }
        } else if (((a === 0) && (a < b)) || ((b === 0) && (b > a))) {
            for (let i = a; i <= b; i++) {
                answer += i;
            }
        }
    }

    return answer;
}

// a	b	return
ex1 = [3, 5]	// 12
ex2 = [3, 3]	// 3
ex3 = [5, 3]	// 12
ex4 = [-3, 5] // 9
ex5 = [-5, 3] // -9
ex6 = [3, -5] // -9
ex7 = [3, -1] // 5
console.log(solution(ex7[0], ex7[1]));