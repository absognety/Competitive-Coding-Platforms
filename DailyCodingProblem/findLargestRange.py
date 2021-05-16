"""
This problem was asked by Airbnb.

Given an array of integers, return the largest range, 
inclusive, of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], 
return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.

"""

def find_largest_range(arr):
    max_element = max(arr)
    all_ranges = []
    for a in sorted(arr):
        i = a
        collect_ranges = []
        while (i <= max_element):
            if i in arr:
                collect_ranges.append(i)
            else:
                break
            i += 1
        all_ranges.append(collect_ranges)
    sorted_ranges = sorted(all_ranges,key=lambda r: len(r),reverse=True)
    print (sorted_ranges)
    return (sorted_ranges[0][0],sorted_ranges[0][-1])
    
if __name__ == '__main__':
    arr = [9,6,1,3,8,10,12,11]
    print (find_largest_range(arr))
    
    arr = [0,5,8,9,23,24,25,34,40,41,42,43]
    print (find_largest_range(arr))