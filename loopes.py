x=1
while x<=10:
    print(x)
    x+=1



x=0
while x<10:
    print('x is currently:',x)
    print('x is still less than 10,adding 1 to x')
    x+=1
    if x==3:
        print('breaking because x==3')
        break
    else:
        print('continuing...')
        continue


x=0
while x<10:
    print('x is currently:',x)
    print('x is still less than 10,adding 1 to x')
    x+=1
    if x==3:
        print('breaking because x==3')

    else:
        print('continuing...')
        continue




for x in range(0,10):
    print(x)


name='salmon'
for i  in name:
    print(i)




for x in range(0,25,2):
    print(x)


for x in range(5):
    print(x)




r=float(input("enter r value "))
p=3.14
area_of_the_circle = p*(r**2)

print("area of the circle is",area_of_the_circle)



for i in  range(0,50):

    if(i%2!=0):

        print("",i)



for i in range(10,0,-1):
    print(i)



for i in range (100,0,-10):
    print(i)




name='salman'
for a in name:
    if 's'not in name:
        print('yes')
    else:
        print('no')