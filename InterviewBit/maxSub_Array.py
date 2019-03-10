class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self,A):
        subArrays = []
        for i in range(len(A)):
            if A[i]>=0:
                subArrays.append([A[i]])
        new_subArrays = []
        for skipper in range(2,len(A)+1):
            for i in range(len(A)):
                new_subArrays.append(A[i:i+skipper])
        unique_subArrays = []
        for arr in new_subArrays:
            if arr not in unique_subArrays:
                unique_subArrays.append(arr)
        disposed = []
        for x in range(len(unique_subArrays)):
            if len(unique_subArrays[x]) == 1:
                disposed.append(unique_subArrays[x])
        for y in disposed:
            unique_subArrays.remove(y)
        all_subArrays = subArrays + unique_subArrays
        filtered_Arrays = []
        for a in all_subArrays:
            abs_Array = [abs(i) for i in a]
            if abs_Array == a:
                filtered_Arrays.append(a)
        if filtered_Arrays:
            sum_Array = [sum(arr) for arr in filtered_Arrays]
            maximumSum = max(sum_Array)
            if sum_Array.count(maximumSum) == 1:
                ind = sum_Array.index(maximumSum)
                return (filtered_Arrays[ind])
            else:
                inds = []
                for i,s in enumerate(sum_Array):
                    if s == maximumSum:
                        inds.append(i)
                maxArrayLens = [len(filtered_Arrays[Ind]) for Ind in inds]
                maximumLen = max(maxArrayLens)
                if maxArrayLens.count(maximumLen) == 1:
                    len_ind = maxArrayLens.index(maximumLen)
                    return (filtered_Arrays[len_ind])
        else:
            print ()
            
if __name__ == '__main__':
    A = list(map(int,input().strip().split()))
    solution = Solution()
    print (solution.maxset(A))
                               