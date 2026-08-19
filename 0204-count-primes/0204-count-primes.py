class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return 0
        prime = [1]*(n)
        prime[0]=prime[1]=0
        for i in range(2,int(n**0.5)+1):
            if prime[i]==1:
                length_of_slice = (n - 1 - i*i) // i + 1
                prime[i*i : n : i] = [0] * length_of_slice
                # for j in range(i*i,n,i):
                #     prime[j]=0
        return sum(prime)