# nlog(n) used in python sort() deafault function


def split(array):
    midpoint = len(array)//2
    if len(array)>1:
        array1 = array[:midpoint]
        array2 = array[midpoint:]    
        array1 = split(array1)
        array2 = split(array2)
        array = merge_sorted(array1,array2)
    return array


def merge_sorted(array1, array2):
    i=0
    j=0
    array=[]
    while i<len(array1) and j<len(array2):
        if array1[i]>array2[j]:
            array.append(array2[j])
            j+=1
        else:
            array.append(array1[i])
            i+=1
        
    while i < len(array1):
        array.append(array1[i])
        i+=1
    
    while j < len(array2):
        array.append(array2[j])
        j+=1
    return array

array1 = [1,2,3,4]
array2 = [4,5,6]
print(split(array1))