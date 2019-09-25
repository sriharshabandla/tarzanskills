 age=int(input("enter age"))
 if age >=18:
     print(f'{age} is my age so i am eligible for voting')
 else:
     print(f'{age}is my age so i am not eligible')

 marks=int(input("enter your marks"))
 if marks >=90 and marks <=100:
     print(f'{marks} grade-A')
 elif marks >=80 and marks <=90:
     print(f'{marks} grade-B')
 elif marks >=70 and  marks <=80:
     print(f'{marks} grade-C')
 else:
     print(f'{marks} grade-D')

 number=int(input('enter number:'))
 if number%2==0 :
     print(f'{number} even number')
 else:
     print(f'{number} odd number')


num=int(input("enter number"))
if (num>0):
    if(num==0):
        print("zero")
    else:
        print("negative")




x=input('name')
print(x)
if 's' in x:
    if 'z'in x:
        print('yes')
    else:
        print('no')
else:
    print('not')