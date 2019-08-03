class Solution:
     def reverse(self, x: int) -> int:
        result = 0
        neg_flag = False
        if x == 0:
            return 0
        if x < 0:
            neg_flag = True
            x *= -1
        while x > 0:
            result *= 10
            result += x % 10
            x = x - (x % 10)
            x = x / 10
        if neg_flag:
            result *= -1
        if result > 2**31-1 or result < -2**31-1:
            return 0
        return int(result)

test = Solution()
print("123 = " + str(test.reverse(123)))
print("-123 = " + str(test.reverse(-123)))
print("120 = " + str(test.reverse(120)))
print("1534236469 = " + str(test.reverse(1534236469)))
