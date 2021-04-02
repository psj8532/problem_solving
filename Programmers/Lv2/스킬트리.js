function solution(skill, skill_trees) {
    const skillArr = [...skill];
    return skill_trees
        .map(skillTree => (
            [...skillTree]
                .filter(skill => ~skillArr.indexOf(skill))
                .join('')
        ))
        .filter(skillTree => {
            const newSkill = skill.slice(0, skillTree.length);
            return newSkill === skillTree;
        })
        .length;
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))