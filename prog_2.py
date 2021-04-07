""" 2. Write a program to sort the elements in odd positions in descending order and elements in ascending order

Eg 1: Input: 13,2 4,15,12,10,5
        Output: 13,2,12,10,5,15,4
Eg 2: Input: 1,2,3,4,5,6,7,8,9
        Output: 9,2,7,4,5,6,3,8,1  """

arr=list(map(int,input().split()))
odd_pos=arr[::2]
even_pos=arr[1::2]
odd_pos.sort()
even_pos.sort(reverse=True)

while len(odd_pos)>0 and len(even_pos)>0:
    print(odd_pos.pop(),end=' ')
    print(even_pos.pop(),end=' ')
print(' '.join(str(i) for i in odd_pos))