def quick_sort(array,low,high):
    if low<high:
    return array

def hoare(array,low,high):
    i= 0
    j= len(array)-1
    pivot = array[pivotidx]
    while i<j:
        while array[i] < pivot:
            i+=1
        while array[j] > pivot:
            j-=1
        
        array[i] , array[j] = array[j], array[i]
    return j 


array = [7,1,4,6,5,8,9]
array = quick_sort(array,0,len(array)-1)
print(array)