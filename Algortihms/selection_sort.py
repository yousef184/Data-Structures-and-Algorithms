#O(N^2)

def min(array):
    min = 100000
    index =0
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
            index = i
    return index
        
def selection_sort(array):
    for i in range(len(array)):
        index =  min(array[i:]) +i
        array[i],array[index] = array[index], array[i]
    return array



array = [7,1,4,2,3,6,5,9,8]
array = selection_sort(array)
print(array)
