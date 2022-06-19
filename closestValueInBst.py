#average O(log(n))| worst O(n) time and O(1) space

#recursive solution
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None: 
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)

    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    
    else:
        return closest


#iterative solution
def findClosestValueInBstRec(tree, target):
    return findClosestValueInBstHelperRec(tree, target, float('inf'))

def findClosestValueInBstHelperRec(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left

        elif target > currentNode.value:
            currentNode = currentNode.right
        
        else:
            break

    return closest