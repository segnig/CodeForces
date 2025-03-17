""" Description

For a given arr find all subsequence that has k sum
:= return all subsequences

"""
class Solution:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.k_sum_subsequences = []
        
    def k_sum_subsequences_finder(self, sum_of_subsequence=0, subsequence=[], index=0):
        if index == len(self.arr):
            if sum_of_subsequence == self.k:
                self.k_sum_subsequences.append(subsequence[:])
            return []
        
        # take     
        subsequence.append(self.arr[index])
        self.k_sum_subsequences_finder(sum_of_subsequence+self.arr[index], subsequence, index=index+1)
        
        # not take
        subsequence.pop()
        self.k_sum_subsequences_finder(sum_of_subsequence, subsequence, index=index+1)
        return self.k_sum_subsequences
    
 
arr = [5, 4, 2, 2, 4, 5, 6, 0, 5, 5, 5, 2, 1, 56, 0, 23]
sol = Solution(arr=arr, k=5)
print(sol.k_sum_subsequences_finder())