# def check(n):
#     if n%2==0:
#       print("even")
#     else:
#         print("odd")
#     return n

# check(4)


# def sum_of_number(num1=20,num2=30):
#
#     result=num1+num2
#     return result
# print(sum_of_number())


# n=int(input('enter n value : '))
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         X = n*fact(n-1)
#         return X
#
# print(fact(n))




# def greet(name,msg='good morning'):
#     print(f'hi{name} {msg}')
# greet('salman')


#
# def greet(*names):
#     for name in names:
#         print(f'hi{name}')
# greet('salman','praveen','harsha')


# def function(**kwargs):
#     if 'fruit' in kwargs:
#         print(f" {kwargs['fruit']}")
# function(fruit='apple')

#
# def function(*args):
#     for name in args:
#         print(name)
# function('apple', 'orange')
#
#
#
# def function (**kwargs)
#     if 'furniture' in kwargs:
#         print(f'hi{kwargs}')



# def myfunc(**kwargs):
#   if 'fruit' and 'juice' in kwargs:
#     print(f"my favourite fruit is{kwargs['fruit']},and juice is {kwargs['juice']}")
#   else:
#     print("i don't like fruit")
# myfunc(fruit='pineapple',juice='orange')




# first_name="salman"
# second_name="ahmed"
# result=str(first_name+second_name)
#
# print(result[::-1])



def grossary(**kwargs):
    if 'quantity' and 'item'  and 'price 'in kwargs:
        print(f"arguments of quantity{kwargs['quanty']},and price is{kwargs['price']}")
    else:
        print("i am not purchase")
grossary(quantity='1',price=2)

