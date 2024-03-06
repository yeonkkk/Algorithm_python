import sys

'''
문제: 스티커 (실버1)
분류: dp
'''

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if 1 < n: 
        dp[0][1] = stickers[0][1] + stickers[1][0] 
        dp[1][1] = stickers[1][1] + stickers[0][0]

    for i in range(2, n):
        dp[0][i] = stickers[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = stickers[1][i] + max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][n-1], dp[1][n-1]))