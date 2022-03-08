from random import randint
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        self.quicksort(A, 0, len(A)-1)
        return A
    
    def quicksort(self, A, start, end):
        if start >= end:
            return
        pivot = randint(start, end) # generate random pivot index and swap with A[start] for randomized pivot
        A[pivot], A[start] = A[start], A[pivot]
        pivot = self.partition(A, start, end)
        self.quicksort(A, start, pivot-1)
        self.quicksort(A, pivot+1, end)
        return
    
    def partition(self, A, start, end):
        pivot = start
        start += 1
        while start <= end:
            if A[start] <= A[pivot]:
                start += 1
            elif A[end] > A[pivot]:
                end -= 1
            else:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        A[pivot], A[start-1] = A[start-1], A[pivot]
        return start -1