""" 3. Write a program to print the following output for the given input. You can assume the string is of odd length

Eg 1: Input: 12345
       Output:
1       5
  2   4
    3
  2  4
1      5
Eg 2: Input: geeksforgeeks
         Output:
g                         s
  e                     k
    e                 e
      k             e
        s         g
          f      r
             o
          f     r
        s         g
      k             e
    e                 e
  e                      k
g                          s  """

string=input().split()
widht=len(string)*2-1
for i in range(len(string)//2):
    print('  '*i+string[i]+' '*(len(string)*2-i*2)+string[-i-1])
print(string[len(string)//2].center(len(string)*2,' '))
for i in range(len(string)//2+1,len(string),1):
  print('  '*i+string[i]+' '*(len(string)*2-2-1-i)+string[-i-1])
