def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def mergeSort(arr):
    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def quickSort(arr):
    def partition(arr, left, right):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left
    def _quickSort(arr, left, right):
        if left < right:
            p = partition(arr, left, right)
            _quickSort(arr, left, p - 1)
            _quickSort(arr, p, right)
    _quickSort(arr, 0, len(arr) - 1)
    return arr

def heapSort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    def buildHeap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
    buildHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def countingSort(arr):
    maxValue = max(arr)
    count = [0] * (maxValue + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, maxValue + 1):
        count[i] += count[i - 1]
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return result



print(selectionSort([0,9,2,5,3,4,1,6,7,8]))