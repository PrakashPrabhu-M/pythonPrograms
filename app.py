import os,time
def pro():
  os.system('clear')
  print('Welcome'.upper().center(50,'*'))
  run=True
  while run:
    run=False
    name=input("Type your name: ".upper())
    if name=='':
      print('Type Something')
      time.sleep(2)
      os.system('clear')
      run=True
      continue
    for i in name:
      if (97<=ord(i)<=122) or (65<=ord(i)<=90):
        pass
      else:
        print('Invalid characters are present')
        print('Try again')
        time.sleep(2)
        os.system('clear')
        run=True
      continue
  run=True
  while run:
    run=False
    try:
      ph=int(input('Type your number: '.upper()))
    except ValueError as e:
      print('Invalid characters')
      print('Try again')
      time.sleep(2)
      os.system('clear')
      run=True
      continue
    if ph<0:
      print('Negative numbers')
      print('Try again')
      time.sleep(2)
      os.system('clear')
      run=True
      continue
  l=[]
  def trav():
    run=True
    
    while run:
      run=False
      try:
        l.insert(1,float(input('Enter your source: '.upper())))
      except ValueError as e:
        print('Invalid\nTry again')
        run=True
        continue
    run=True
    while run:
      run=False
      try:
        l.insert(1,float(input('Enter your destination: '.upper())))
      except ValueError as e:
        print('Invalid\nTry again')
        run=True
        continue
  trav()
  for i in l:
    if i<0:
      print('Invalid')
      print('Try again')
      time.sleep(2)
      os.system('clear')
      pro()

  dist=abs(l[0]-l[1])
  if dist==0:
    print('Nothing to'.upper())
    print('Try again')
    trav()

  print('Choose your choice with number'.upper().center(50,'*'))
  print('1.bike => {0}rs{3}2.car => {1}rs{3}3.Premium => {2}rs{3}'.format(5,10,15,'\n'))
  
  def cal():
    try:
      choice=round(float(input()))
    except ValueError as e:
      print('Type a number....\nTry again')
      time.sleep(2)
      pro()
    if choice==1:
      return dist*5,'bike'
    elif choice==2:
      return dist*10,'car'
    elif choice==3:
      return dist*15,'Premium'
    else:
      print('Invalid Choice....\nTry again')
      time.sleep(2)
      pro()
      
  cost,vec=cal()

  print('Finalization'.center(50,'*'),'\n')
  print('NAME: {} \t\tPHONE NUMBER: {}\nSOURCE: {} \t\tDESTINATION: {} \nCATAGORIE: {} \n\nTOTAL COST: {} rs'.format(name,ph,l[0],l[1],vec,cost))
  time.sleep(100)
  pro()
pro()
