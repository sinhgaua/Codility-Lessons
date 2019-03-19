"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""
A = [1, 3, 6, 4, 1, 2]
B= [1, 2, 3]
C=[-1,-3]

def solution(A):
    counter = [False]*len(A)
    for item in A:
        if 0<item<=len(A):
            counter[item-1]= True
    for idx in range(len(counter)):
        if counter[idx]==False:
            return idx+1
    return len(A)+1

print (solution(A))
print (solution(B))
print (solution(C))
