
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    combi = [[] for _ in range(n+1)]
    combi[0] = [0]
    for i in range(n):
        for c in combi[i]:
            combi[i + 1].append(c + numbers[i])
            combi[i + 1].append(c - numbers[i])

    return combi[n].count(target)
'''
# DFS
def solution(numbers, target):
    answer = 0

    def dfs(index, total):
        nonlocal answer
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    
    dfs(0, 0)
    return answer
'''