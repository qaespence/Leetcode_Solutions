class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for char in address:
            if char == ".":
                result += "[.]"
            else:
                result += char
        return result

test = Solution()
print("Input: 1.1.1.1")
print("Result: " + test.defangIPaddr("1.1.1.1"))
