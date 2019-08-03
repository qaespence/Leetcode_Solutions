class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Using merge sort
        # Time : O(NlogN)
        # Space : O(NlogN)
        if len(nums) == 1:
            return nums

        mid = int(len(nums)/2)
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        return self.mergeSort(self.sortArray(leftHalf), self.sortArray(rightHalf), nums)

    def mergeSort(self, leftHalf, rightHalf, nums):
        i, j , k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                nums[k] = leftHalf[i]
                i += 1
            else:
                nums[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            nums[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            nums[k] = rightHalf[j]
            j += 1
            k += 1
        return nums

test = Solution()
print("[5,2,3,1]: " + str(test.sortArray([5,2,3,1])))
print("[5,1,1,2,0,0]: " + str(test.sortArray([5,1,1,2,0,0])))
print("[5,1,1,-2,0,0,-7,100,-250,6,-18,18]: " + str(test.sortArray([5,1,1,-2,0,0,-7,100,-250,6,-18,18])))
