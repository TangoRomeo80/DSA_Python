class Solution:
    def findComplement(self, num: int) -> int:
        # # convert num to binary
        # binary = bin(num)[2:]
        # # convert binary to string
        # binary = str(binary)
        # # replace 0 with 1 and 1 with 0
        # newStr = []
        # for i in binary:
        #     if i == '0':
        #         newStr.append('1')
        #     else:
        #         newStr.append('0')
        # # convert back to binary
        # newStr = ''.join(newStr)
        # # convert back to int
        # return int(newStr, 2)

        mask = 1
        while mask < num:
            mask = (mask << 1) + 1
        return num ^ mask
        

