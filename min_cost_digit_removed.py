def min_worth_digit_removed(string, worth):
    n = len(string)
    dp=[[0]*2 for _ in range(n)]
    dp[0][0]=worth[0] if string[0]=='0' else 0
    dp[0][1]=worth[0] if string[0]=='1' else 0
    for i in range(1,n):
      if string[i]=='0':
        dp[i][0]=max(dp[i-1][1] + worth[i], dp[i-1][0])
        dp[i][1]=dp[i-1][1]
      else:
        dp[i][1]=max(dp[i-1][0] + worth[i], dp[i-1][1])
        dp[i][0]=dp[i-1][0]
    max_worth=max(dp[n-1])
    total_worth=sum(worth)
    removed_worth=total_worth-max_worth
    return removed_worth
string = input().strip()
worth = list(map(int, input().split()))
print(min_worth_digit_removed(string, worth))