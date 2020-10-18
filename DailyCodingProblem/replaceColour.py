"""
Daily Coding Problem #151

Given a 2-D matrix representing an image, a location of a pixel 
in the screen and a color C, replace the color of the given pixel 
and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel 
of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B

"""
def replaceColourUtil(arr,p,q,prevC,newC):
    if ((p < 0) | (p >= M) | (q < 0) | (q >= N)):
        return
    if arr[p][q] != prevC:
        return
    if arr[p][q] == newC:
        return
    
    arr[p][q] = newC
    
    # Recur for north, east, south and west
    replaceColourUtil(arr, p+1, q, prevC, newC)
    replaceColourUtil(arr, p-1, q, prevC, newC)
    replaceColourUtil(arr, p, q+1, prevC, newC)
    replaceColourUtil(arr, p, q-1, prevC, newC)
    

def replace_colour(matrix,a,b,color):
    prevC = matrix[a][b]
    replaceColourUtil(matrix, a, b, prevC, color)
    
    
if __name__ == '__main__':
    for tcase in range(int(input())):
        arr = []
        for row in range(int(input())):
            r = input().strip().split()
            arr.append(r)
        location = list(map(int,input().strip().split()))
        color = input().strip()
        M,N = len(arr),len(arr[0])
        a,b = location[0],location[1]
        replace_colour(arr,a,b,color)
        print (arr)