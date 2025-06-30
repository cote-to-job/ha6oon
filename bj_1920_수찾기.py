import sys
input = sys.stdin.readline

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
targets = list(map(int, input().split()))

for x in targets:
    print(binary_search(a, x))

