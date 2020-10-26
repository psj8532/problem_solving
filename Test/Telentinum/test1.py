def balancedSum(arr):
    # Write your code here
    N = len(arr)
    for i in range(1,N-1):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            return i


ex1 = [1, 2, 3, 3]
ex2 = [1, 2, 1]
print(balancedSum(ex2))