class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # return [int(x) for x in str(int(''.join([str(x) for x in num])) + k)]
        res = []
        carry = 0
        i = len(num) - 1
        while i >= 0 or k > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            if k > 0:
                carry += k % 10
                k //= 10
            res.append(carry % 10)
            carry //= 10
        if carry:
            res.append(carry)

        return res[::-1]
        
