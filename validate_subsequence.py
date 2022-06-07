# O(n) time O(1) space
def validateSubsequence(array, sequence):
    sequence_index = 0
    for num in array:
        if num == sequence[sequence_index]:
            sequence_index += 1
            if sequence_index == len(sequence):
                return True
    return False

arr = [5, 1, 4, 2, 8]
seq = [1, 2, 8]

# print(validateSubsequence(arr, seq))