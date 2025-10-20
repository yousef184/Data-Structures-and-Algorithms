def hoare(array):
    i= 0
    j= len(array)-1
    pivot = array[0]
    while i<j:
        while array[i] < pivot:
            i+=1
        while array[j] > pivot:
            j-=1
        
        array[i] , array[j] = array[j], array[i]
    return array


array = [7,1,4,6,5,8,9]
array = quick_sort(array)
print(array)
