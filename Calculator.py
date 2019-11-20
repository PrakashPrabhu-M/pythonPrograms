print('WELCOME'.center(50,'*'))
run=1
while run:
    run2=run3=1
    while run2:
        try:
            ch=int(input('Enter your choice\n1.Add\n2.Subtract\n3.Division\n4.Multiplication\n'+'0 to exit'.center(50,'*')+' '))
            run2=0
        except ValueError:
            print('Only an integer is expected')
    while run3:
        run3=0
        try:
            if ch==1:
                print(float(input('Type the first number: '))+float(input('Type the second number: ')))
            elif ch==2:
                print(float(input('Type the first number: '))-float(input('Type the second number: ')))
            elif ch==3:
                print(float(input('Type the first number: '))/float(input('Type the second number: ')))
            elif ch==4:
                print(float(input('Type the first number: '))*float(input('Type the second number: ')))
            elif ch==0:
                run=0
                break
            else:
                print('Invalid input try again...')
        except ValueError:
            print('Only Numbers are allowed')
            run3=1
