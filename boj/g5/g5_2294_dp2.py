# 입력
import sys, math
input= sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

# dp[i] = i를 만드는 최소의 동전 개수(동전의 가치는 다르거나 같음)
dp = [math.inf for _ in range(k+1)]

# 계산1: 초기화
dp[0] = 0

# 계산2: dp
for i in range(1, k+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 출력
if dp[k] == math.inf:
    print(-1)
else:
    print(dp[k])