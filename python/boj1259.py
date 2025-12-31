import sys
results = []
while True:
    str = input().strip()
    if str == '0':
        break
    if str == str[::-1]:
        results.append("yes")
    else:
        results.append("no")
for res in results:
    print(res)