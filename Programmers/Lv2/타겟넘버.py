# 11:42 ~ 12:01
def solution(numbers, target):
    answer = 0

    def dfs(depth, total, ans):
        if depth == len(numbers):
            if total == target:
                ans += 1
            return ans

        ans = dfs(depth + 1, total - numbers[depth], ans)
        ans = dfs(depth + 1, total + numbers[depth], ans)
        return ans

    answer = dfs(0, 0, answer)
    return answer

# numbers	target	return
ex1 = [[1, 1, 1, 1, 1],	3]	# 5
print(solution(*ex1))