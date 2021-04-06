const solution = (numbers) => {
    let answer = 0;
    const primes = {};
    const perm = [];
    const permutation = (k, a, permSize, totalSize) => {
        if (k === permSize) {
            const temp = a.map(v => v);
            perm.push(temp);
            return;
        }

        const inPerm = new Array(totalSize).fill(false);

        for (let i = 0; i < k; i++) {
            inPerm[a[i]] = true;
        }

        const c = new Array(permSize).fill(0);
        let cnt = 0;
        for (let i = 0; i < totalSize; i++) {
            if (inPerm[i]) continue;
            c[cnt++] = i;
        }

        for (let i = 0; i < cnt; i++) {
            a[k] = c[i];
            permutation(k + 1, a, permSize, totalSize);
        }
    };

    const checkPrime = (num) => {
        if (num <= 1) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    };

    const numbersSize = numbers.length;
    for (let i = 1; i <= numbersSize; i++) {
        permutation(0, new Array(i).fill(0), i, numbersSize);
    }

    perm.forEach(p => {
        let num = p
            .map(pVal => numbers[pVal])
            .join('');
        num = parseInt(num);
        if (checkPrime(num) && !(num in primes)) {
            primes[num] = true;
            answer++;
        }
    });
    return answer;

};

console.log(solution("011"));