import allPathsInaMatrix as aPIM
    
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        R, C = list(map(int,input().strip().split()))
        arr = input().strip().split()
        arrMatrix = []
        for x in range(0,len(arr),C):
            arrMatrix.append(arr[x:x+C])
        aPIM.findPaths(arrMatrix,R,C)
        myPaths = aPIM.storePaths.split('|')
        numPalindromicPaths = 0
        for cpath in myPaths[:len(myPaths)-1]:
            if cpath == cpath[::-1]:
                numPalindromicPaths += 1
        print (numPalindromicPaths)