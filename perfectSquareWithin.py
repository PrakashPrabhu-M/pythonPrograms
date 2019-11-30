""" Given a range i.e., 2 numbers l and r count the number of perfect squares in the range (inclussive of l and r ).
Input Size : l <= r <= 100000(complexity O(n))
Sample Testcase :
INPUT
2 5
OUTPUT
1 """

l,r=[int(x) for x in input().split()]
def perfectSquare(n):
    if n**0.5==int(n**0.5):
        return True
    return False

i=list(range(l+1,r))
sqnums=list(filter(perfectSquare,i))
print(len(sqnums))
