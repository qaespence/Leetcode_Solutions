class Solution:
    def find_largest_three(self, list, N):
        result = []

        for i in range(0,N):
            max = None
            for j in list:
                if max is None:
                    max = j
                    continue
                if max < j:
                    max = j
                    continue
            list.remove(max)
            result.append(max)
        return result

test_list = [2,9,7,8,-1,30,-5,18,1,12]
test = Solution()
print(test.find_largest_three(test_list, 3))
