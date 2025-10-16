#O(n^2)

def bubble_sort(array):
    l = len(array)-1
    for i in range(l):
        for j in range(l-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

array = [7,1,4,2,3,6,5]
array = bubble_sort(array)
print(array)
