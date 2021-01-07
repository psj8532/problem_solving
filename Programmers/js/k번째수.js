function solution(array, commands) {
    return commands.flatMap(command => (
        array
            .slice(command[0] - 1, command[1])
            .sort((a, b) => a - b)
            .filter((val, idx) => idx === command[2] - 1)
    ));
}

// array	commands	return
ex1 = [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]];	//[5, 6, 3]
console.log(solution(ex1[0], ex1[1]));