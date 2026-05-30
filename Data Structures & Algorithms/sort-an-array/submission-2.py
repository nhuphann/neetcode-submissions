class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(array, L, M, R):
            left, right = array[L:M+1], array[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    array[i] = left[j]
                    j += 1
                else:
                    array[i] = right[k]
                    k += 1
                i +=  1
            while j < len(left):
                    array[i] = left[j]
                    i += 1
                    j += 1
            while k < len(right):
                    array[i] = right[k]
                    i += 1
                    k += 1


        def mergesort(array,l,r):
            if l == r:
                return array

            m = (l + r ) // 2

            mergesort(array, l, m)
            mergesort(array, m+1, r)
            merge(array, l , m, r)

            return array

        return mergesort(nums,0, len(nums)-1)

