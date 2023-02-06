#85-----------------------------------------------------------

# def func():
#     a = int(input('Enter a: '))
#     b = int(input('Enter b: '))
#     return (a**2+b**2)**0.5
# print('c = ',func())

#86------------------------------------------------------------

# def func():
#     a = int(input('Enter mile:'))
#     return ((a/140)*0.25)+4
# print('sum = ',round(func(),2))

#87-----------------------------------------------------------

# def func():
#     a = int(input('Enter count:'))
#     return (a-1)*2.95+10.95
# print('sum = ',round(func(),2))

#88------------------------------------------------------------

# def median():
#     a = int(input('Enter a: '))
#     b = int(input('Enter b: '))
#     c = int(input('Enter c: '))
#     median = (a+b+c)/3
#     return median
# print('median = ',median())

#89-------------------------------------------------------------

# def number():
#     num = int(input('Enter number'))
#     numbers = ['','first','second','third','fourth','fifth','sixth',
#                'seventh','eighth','ninth','tenth','eleventh','twelfth']
#     ordinalNumber = numbers[num]
#     return ordinalNumber
# print(number())


#91--------------------------------------------------------------
# def ordinalDate(year,month,day):
#     months = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if year%4 == 0:
#         months[1] +=1
#     num = 0
#     for i in range(month-1):
#         num += months[i]
#     num += day
#     return num

# print(ordinalDate(2004,2,29))

#92---------------------------------------------------------------

# def func(s:str,w:int)->str:
#     if len(s)>=w:
#         return s
#     else:
#         a = (w - len(s))//2
#         return a*'.' + s + (w-len(s)-a)*'.'
# print(func('hello',11))

#94----------------------------------------------------------------

# def func(a,b,c):
   
#     if a == 0 or b == 0 or c == 0:
#         return "False"
#     elif a < b+c and b < a+c and c < a + b:
#         return "true"
#     else: 
#         return "False" 

# A = int(input('Enter a: '))
# B = int(input('Enter b: '))
# C = int(input('Enter a: '))

# print(func(A,B,C))

#95----------------------------------------------------------------

# def func(text):
#     newtext=''
#     newtext += text[0].upper()
#     for i in range(1,len(text)):
#         if text[i-1] in ['.','?','!']:
#             newtext += text[i].upper()
#         else:
#             newtext += text[i]
#     return newtext

# text = input('Enter text: ')
# text = func(text)
# print(text)


#96-------------------------------------------------------------------

# def isInteger(num):
#     for i in range(len(num)):
#         if num[i].isdigit():
#             return'true'
#         elif (num[0] == '-' or num[0] == '+') and num[1::].isdigit():
#             return'true'
#         else:
#             return'false'
        
# num = input('Enter text: ').replace(' ','')
# print(isInteger(num))

#97-------------------------------------------------------------------

# def precedence(m):
#     if m == '+' or m == '-':
#         return'1'
#     elif m == '*' or m == '/':
#         return'2'
#     elif m == '^':
#         return'3'
#     else:
#         return'-1'
# M = input('Enter operator: ')
# print(precedence(M))

#98------------------------------------------------------------------------

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# a = int(input('Enter number: '))
# print(is_prime(a))

#99---------------------------------------------------------------------------
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def next_prime(num):
#     num += 1
#     while not is_prime(num):
#         num += 1
#     return num

# if __name__ == '__main__':
#     n = int(input('Enter a number: '))
#     print(f'The next prime number after {n} is {next_prime(n)}')

#100------------------------------------------------------------------------------
# import random

# def password():
#     pas = ''
#     x = random.randint(7,11)
    
#     for i in range(x):
#         pas+= chr(random.randint(36,126))
    
#     return pas
# print(password())


# 101-------------------------------------------------------------------------------

# import random

# def carnumber():
#     number = ''
#     for i in range(4):
#         number+=str(random.randint(0,9))
#     for j in range(3):
#         number+=chr(random.randint(65,90))
#     return number
# print(carnumber())

#102------------------------------------------------------

# def wildpassword(pas):
#     u = 0
#     l = 0
#     d = 0
#     if len(pas) >= 8:
#         for i in pas:
#             if i.isupper():
#                 u+=1
#             elif i.islower():
#                 l += 1
#             elif i.isdigit():
#                 d += 1
#     if u >= 1 and l >= 1 and d >= 1 and u+l+d == len(pas):
#         return True
#     else:
#         return False
# Pas = input('Enter pasword: ')
# print(wildpassword(Pas))

#103----------------------------------------------------------

# from typing import Callable

# def newpassword():
#     count = 0
#     pas = password()
#     while not wildpassword(pas):
#         pas = password()
#         count += 1
#     print("Generated password:", pas)
#     print('Count:',count)

# print(newpassword())


#104----------------------------------------------------------

# def hex2int(n):
#     a = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
#         '8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#     if n not in a:
#         return False
#     return a[n]
# N = input('Enter num: ').upper()
# print(hex2int(N))

# def int2hex(n):
#    if n not in range(16):
#       return False
#    a = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
#         8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
#    return a[n]
# N = int(input('Enter num: '))
# print(int2hex(N))

#106------------------------------------------------------------------

# def countday(month,year):
#     months = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if year%4 == 0:
#         months[1] = 29
#     return months[month-1]

# Month = int(input('Enter month;'))
# Year = int(input('Enter year: '))
# print(countday(Month,Year))

#107----------------------------------------------------------------------
# def divider(a,b):
#     div=[]
#     for i  in range(1,min(a,b)+1):
#         if (a%i)==0 and (b%i)==0:
#             div.append(i)
#     return div[len(div)-1]

# up = int(input("up num "))

# down = int(input("down num "))

# div = divider(up,down)
# up /= div

# down /= div

# print(up,"/",down)


#108----------------------------------------------------------------------

# def recipe_volumes(volume, unit):
#     cup = 0
#     tbsp = 0
#     tsp = 0
#     if unit == 'cup':
#         cup = volume
#     elif unit == 'tablespoon':
#         tbsp = volume
#         cup = tbsp // 16
#         tbsp = tbsp % 16
#     elif unit == 'teaspoon':
#         tsp = volume
#         tbsp = tsp // 3
#         cup = tbsp // 16
#         tsp = tsp % 3
#         tbsp = tbsp % 16
#     return f"{cup} cup(s), {tbsp} tablespoon(s), {tsp} teaspoon(s)"
# Volume = int(input('Enter volume: '))
# Unit = input('Enter volume: ')
# print(recipe_volumes(Volume,Unit))


#109--------------------------------------------------------------------------


# def is_magic_date(day, month, year):
#     return day * month == year % 100

# def magic_dates_in_20th_century():
#     for year in range(1900, 2000):
#         for month in range(1, 13):
#             for day in range(1, 32):
#                 if is_magic_date(day, month, year):
#                     print(f"{day:02}/{month:02}/{year:04}")
# magic_dates_in_20th_century()
