#O(nlogn) time O(n) space 
def sortedSquaredArrayBrute(array):
    array = sorted(array)
    for i in range(len(array)):
        array[i] = array[i] * array[i]
    return array


#O(n) time O(n) space
def sortedSquaredArrayLinear(array):
    sortedSqures = [0 for _ in array]
    left = 0
    right = len(array) - 1

    for i in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            sortedSqures[i] = array[left] * array[left]
            left += 1
        else:
            sortedSqures[i] = array[right] * array[right]
            right -= 1  
    return sortedSqures

    