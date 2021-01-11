process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    let answer = new Array(b);
    for (let i = 0; i < b; i++) {
        answer[i] = new Array(a).fill('*');
    }
    console.log(answer.map(row => row.join('')).join('\n'));
});