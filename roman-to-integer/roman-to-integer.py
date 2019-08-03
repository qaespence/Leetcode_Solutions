class Solution:
    def roman_to_integer(self, s: str) -> int:
        symbols = [
            ('IV', 4),
            ('IX', 9),
            ('XL', 40),
            ('XC', 90),
            ('CD', 400),
            ('CM', 900),
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]
        result = 0
        for j, k in symbols:
            if j in s:
                result += s.count(j) * k
                s = s.replace(j, '')
        return result

test = Solution()
print("III = " + str(test.roman_to_integer("III")))
print("IV = " + str(test.roman_to_integer("IV")))
print("IX = " + str(test.roman_to_integer("IX")))
print("LVIII = " + str(test.roman_to_integer("LVIII")))
print("MCMXCIV = " + str(test.roman_to_integer("MCMXCIV")))
