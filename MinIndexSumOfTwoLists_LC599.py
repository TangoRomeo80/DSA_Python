class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 1. Create a dictionary of list1
        # 2. Iterate through list2 and check if the restaurant is in the dictionary
        # 3. If it is, add the index sum to the dictionary
        # 4. Find the minimum index sum
        # 5. Return the restaurants with the minimum index sum
        
        # 1. Create a dictionary of list1
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        
        # 2. Iterate through list2 and check if the restaurant is in the dictionary
        # 3. If it is, add the index sum to the dictionary
        dict2 = {}
        for i in range(len(list2)):
            if list2[i] in dict1:
                dict2[list2[i]] = dict1[list2[i]] + i
        
        # 4. Find the minimum index sum
        min_index_sum = min(dict2.values())
        
        # 5. Return the restaurants with the minimum index sum
        return [key for key, value in dict2.items() if value == min_index_sum]