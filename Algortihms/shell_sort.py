
def shell_sort(array,gap):
    if gap >0:
        for i in range(0,len(array)-1,gap):
            j=i+gap
            while i >= 0 and j<len(array):
                if array[i]>array[j]:
                    array[i], array[j] = array[j], array[i] 
                    j=j-gap
                i=i-gap
        gap = gap//2
        shell_sort(array,gap)
    return array


array = [7,1,4,2,3,6,5,9,8]
gap = len(array)//2
array = shell_sort(array,gap)
print(array)