class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        r = s[::-1]
        
        t = [[-1]*(m+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(m+1):
                if i==0 or j==0:
                    t[i][j] = 0
                    
        for i in range(1,m+1):
            for j in range(1,m+1):
                
                if s[i-1] == r[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        
        return t[-1][-1]