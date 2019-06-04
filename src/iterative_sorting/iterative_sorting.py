# TO-DO: Complete the selection_sort() function below 
array = [11,4,8,5,4,5,2,7,1, 100]   

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
    
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # TO-DO: swap
        for x in range(i + 1, len( arr )):
            if arr[smallest_index] > arr[x]:
                smallest_index = x

        arr[i], arr[smallest_index] =  arr[smallest_index], arr[i]



    return arr

print(selection_sort(array))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1):
        for x in range(len( arr ) - 1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]

    return arr

print(bubble_sort(array))
# array = [4,8,5,4,5,2,7,1]  


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr