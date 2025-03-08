n = 100
memo = (n+1)*[-1]

def memoizationFib(n):
    if memo[n] != -1:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return n
    else:
        result = memoizationFib(n-1) + memoizationFib(n-2)
        memo[n] = result
        
    return result 
    
# If i understand, we are going to construct the fib bottom up    
def dpIterativeFib(n):
    fibArr = (n+1) * [0]
    fibArr[0] = 0
    fibArr[1] = 1
    for i in range (2, n+1):
        fibArr[i] = fibArr[i-1] + fibArr[i-2]
    
    return fibArr[n]
        
# print(memoizationFib(40))

def plainRecursiveFib(n):
    if(n == 0):
        # base case
        return 0
    elif (n == 1):
        # base case 2
        return 1
    else:
        # recursive case
        return (plainRecursiveFib(n - 1) +  	 
                plainRecursiveFib(n - 2))
        
        
def longestCommonSubsequence(A, B):
    # Get the length of each input string.
    m = len(A)
    n = len(B)
    # Initialize a 2D array to store the LCS lengths.
    # dp[i][j] will contain the length of LCS of prefixes
    #A[0..i-1] and B[0..j-1].
    dp=[(n + 1)*[0] for i in range(m + 1)]
    #print(dp)
    # Loop through each cell in the 2D array.
    for i in range(m+1):
        for j in range(n+1):
            # Base case: If either of the strings is empty, LCS length is 0.
            if(i == 0 or j == 0):
                dp[i][j] = 0
            # If the corresponding characters in A and B are equal,
            # then we can extend the LCS for A[0..i-2] and B[0..j-2] by 1.
            elif(A[i-1] == B[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            # If the corresponding characters in A and B are different,
            # take the maximum LCS length between A[0..i-1] &
            # B[0..j-2] or A[0..i-2] & B[0..j-1].
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # The value at dp[m][n] contains the length of LCS for A and B.
    return dp[m][n]


if __name__ == "__main__":    
    # print(plainRecursiveFib(40))
    # print(memoizationFib(100))
    # print(dpIterativeFib(40))
    string1="edward"
    string2="supercalifragilisticexpialidocious"
    print("The longest common subsequence between",string1,"and",string2,"is:",end=' ')
    print(longestCommonSubsequence(string1,string2))
