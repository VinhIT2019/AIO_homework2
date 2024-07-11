#4. Khoảng cách Levenshtein.
def levenshtein(source,target):
  dp = [[0 for _ in range(len(target)+1)] for _ in range(len(source)+1)]
  for i in range(len(source)+1):
    dp[i][0] = i
  for j in range(len(target)+1):
    dp[0][j] = j
  for i in range(1, len(source)+1):
    for j in range(1, len(target)+1):
      if source[i-1] == target[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

  return dp[-1][-1]

print(levenshtein('yu', 'you'))
print(levenshtein('kitten', 'sitting'))