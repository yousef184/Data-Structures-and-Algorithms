#Lomoto partition


def quick_sort(array):
    pivote = array[len(array)-1]
    i = -1
    j = 0
    while j < len(array)-1:     
        if array[j] < pivote:
            i+=1
            array[i], array[j] = array[j], array[i]
        j+=1

    i+=1
    array[i], array[len(array)-1] = array[len(array)-1], array[i]
    
    return array
        
            

array = [5,4,1,3]
array = quick_sort(array)
print(array)