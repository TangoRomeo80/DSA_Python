class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        hex_dict = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        hex_str = ""
        while num > 0:
            remainder = num % 16
            if remainder < 10:
                hex_str += str(remainder)
            else:
                hex_str += hex_dict[remainder]
            num = num // 16
        return hex_str[::-1]