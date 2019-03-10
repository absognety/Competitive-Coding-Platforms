class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num_string = ''.join(str(i) for i in A)
        num = int(num_string)
        num = num + 1
        num = str(num)
        final_arr = list(num)
        return (final_arr)
    
if __name__ == '__main__':
    A = list(map(int,input().strip().split()))
    solution = Solution()
    print (solution.plusOne(A))