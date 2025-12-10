import sys
input = sys.stdin.readline
n = int(input())
serial = [input().rstrip() for _ in range(n)]
def ch_sum(s: str) -> int:
    sum = 0
    for ch in s:
        if ch.isdigit():
            sum += int(ch)
    return sum
def key(s: str):
    return (len(s),ch_sum(s),s)
serial.sort(key = key)
for i in serial:
    print(i)
