class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # for i in range(1, n):
        #     if '0' not in str(i) and '0' not in str(n-i):
        #         return [i, n-i]

        def check(num):
            while num>0:
                if num%10==0:
                    return False
                num//=10
            return True
        for i in range(1,n):
            t=n-i
            if check(t) and check(i):
                return [i,t]

                