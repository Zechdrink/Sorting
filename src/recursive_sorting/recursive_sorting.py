# TO-DO: complete the helpe function below to merge 2 sorted arrays
array = [3, 5, 7, 2, 9, 1, 4, 10]
array2 = [3, 5, 7, 2, 9, 1, 4, 10]
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    mergedArray = []
    i,j = 0,0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            mergedArray.append(arrA[i])
            i+=1
        else:
            mergedArray.append(arrB[j])
            j+=1
    mergedArray += arrA[i:]
    mergedArray += arrB[j:]
    return mergedArray


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    half = int(len(arr)/2)
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)

print(merge_sort(array))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
