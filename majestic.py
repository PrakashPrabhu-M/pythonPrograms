'''


Youaregivengiventaskistoprintwhetherarrayis‘majestic’ornot.A‘majsetic’arrayisanarraywhosesumoffirstthreenumberisequaltolastthreenumber.

InputDescription:
Youaregivenanumber‘n’,Nextlinecontains‘n’spaceseparated

OutputDescription:
Print1ifarrayismajesticand0ifitisnot

SampleInput:
7
1234600

SampleOutput:
1

'''
input()
arr=list(map(int,input().split()))
def magestic(l):
    first=last=0
    for i in l[:3]:
        first+=i
    for i in l[-1:-4:-1]:
        last+=i
    if  first==last:
	    print(1)
    else:
	    print(0)
magestic(arr)
