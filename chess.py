""" Aleena is playing chess. She wants to create a program for the game of chess as she is a programmer. 
She creates an 8x8 matrix with the positions of all the pieces. 
For testing purpose, she places a white bishop on an arbitrary location and a black pawn on another arbitrary location. 
Determine if the bishop will cut the pawn in its next move.

 

Input Description:
Locations of the bishop followed by location of the pawn.

Output Description:
Yes, if it will cut. No, otherwise.

Sample Input :
0 1
3 4

Sample Output :
Yes """
def check(m1,m2):
  l1=m1[:]
  l2=m2[:]
  while l1[0]!=0 and l1[1]!=0:
    l1[0]-=1
    l1[1]-=1
  while l2[0]!=0 and l2[1]!=0:
    l2[0]-=1
    l2[1]-=1
  if l1==l2:
    return True
  else:
    l1=m1[:]
    l2=m2[:]
    while l1[0]!=7 and l1[1]!=7:
      l1[0]+=1
      l1[1]+=1
    while l2[0]!=7 and l2[1]!=7:
      l2[0]+=1
      l2[1]+=1
    if l1==l2:
      return True
    return False
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print('Yes' if check(l1,l2) else 'No')
