function solution(a, b) {
    const monthDays = [
        0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ];
    const dayOfWeek = [
        "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"
    ];
    const start = 5;
    if (a > 2) {
        let days = 0;
        for (let i = 1; i < a; i++) {
            days += monthDays[i];
        }
        days += (b - 1);
        return dayOfWeek[(start + days) % 7];
    } else if (a == 2) {
        return dayOfWeek[(start + (31 + b - 1)) % 7];
    } else {
        return dayOfWeek[(start + (b - 1)) % 7];
    }
}

ex1 = [5, 24]; // "TUE"
ex2 = [1, 2];
console.log(solution(ex2[0], ex2[1]));