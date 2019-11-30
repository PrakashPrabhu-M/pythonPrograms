""" 

The Tower of Hanoi (also called the Tower of Brahma) is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

-Only one disk can be moved at a time.

-Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.

-No larger disk may be placed on top of a smaller disk.

You are given the number of disks N. (Here 1 <= N <= 20)

Find the minimum number of moves required to solve the puzzle.

Input Description:
The only line of input contains an integer N

Output Description:
Print a single line, the minimum number of moves.

Sample Input :
3

Sample Output :
7

 """

""" def TOH(s,a,d,n):
    if n==1:
        print('Move the',n,'disk form',s,'to',d)
        return
    TOH(s,d,a,n-1)
    print('Move the',n,' disk from',s,'to',d)
    TOH(a,s,d,n-1)
    
n=int(input())
TOH('source','auxilary','destination',int(n)) """

c=0
def toh(s,a,d,n,c):
    if n==1:
        print('Move the',n,'disk form',s,'to',d)
        globals()['c']+=1
        return
    toh(s,d,a,n-1,c)
    print('Move the',n,'disk form',s,'to',d)
    globals()['c']+=1
    toh(a,s,d,n-1,c)

toh('Source','Auxilary','Destination',3,0)
print(c)
