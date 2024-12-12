'''We are tasked with constructing a string 
X using substrings from a string Y or its reversed version Y rev.There are costs associated with using substrings from 
Y and Y rev, given as S and R respectively. The goal is to determine the minimum cost to construct X. If it's impossible, the function should return "Impossible".'''
def min_string_factor(X, Y, S, R):
    n = len(X)
    m = len(Y)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  
    
    # Reversed Y for checking reversed substrings
    Y_rev = Y[::-1]
    
    for i in range(n):  
        for j in range(m):  
            # Check substrings from Y
            for k in range(1, m - j + 1):  # length of substring
                if i + k <= n and X[i:i + k] == Y[j:j + k]:
                    dp[i + k] = min(dp[i + k], dp[i] + S)
                    
            # Check substrings from reversed Y
            for k in range(1, j + 1):  # length of substring from reversed Y
                if i + k <= n and X[i:i + k] == Y_rev[m - j:m - j + k]:
                    dp[i + k] = min(dp[i + k], dp[i] + R)

    # The result is the minimum factor to form the whole string X
    result = dp[n]
    return result if result != float('inf') else "Impossible"


X = input().strip()
Y = input().strip()
S, R = map(int, input().split())
result = min_string_factor(X, Y, S, R)
print(result)