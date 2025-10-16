def insertion_sort(array):
    for i in range(len(array)-1):
        j=i+1
        while i >= 0:
            if array[i]>array[j]:
                array[i], array[j] = array[j], array[i] 
                j=j-1
            i=i-1
    return array


array = [7,1,4,2,3,6,5]
array = insertion_sort(array)
print(array)