#log(n)
from t_dec import tik

@tik
def binary_search(array,number):
    r = len(array) -1
    l = 0
    while l<=r:
        m = (l+r)//2
        # print(m)
        if number > array[m]:
            l = m+1
        elif number < array[m]:
            r = m-1
        else:
            return True
    return False

array = [1,2,3,4,5,6]
print(binary_search(array, 7))