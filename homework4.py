#1---------------------------------------------------

# def summ(n):
#     suum = 0
#     for i in range(n+1):
#         suum += i
#     return suum
# n = int(input('Enter number: '))    
# print(summ(n))

#2-------------------------------------------------------

# def positive():
#     print("Положительное")

# def negative():
#     print("Отрицательное")

# def test():
#     num = int(input("Введите целое число: "))
#     if num > 0:
#         positive()
#     else:
#         negative()

# test()

#3-----------------------------------------------------------

# import testfunc
# num = []
# while True:
#     n = input('Enter number: ')
#     if n == '':
#         break
#     else:
#         num.append(int(n))
# operator = input('Enter operator: ')

# if operator == '+':
#     result = testfunc.suum(num)

# elif operator == 'max':
#     result = testfunc.maximum(num)

# elif operator == 'min':
#     result = testfunc.minimum(num)

# print(result)

#4-----------------------------------------------


# def revers(num):
#     number = ''
#     for i in num[::-1]:
#         number += i
#     return number
# num = input('Enter numbers: ')
# print(revers(num))


#5---------------------------------------------------

# def count_letters(text):
#     n = 0
#     k = 0
#     for i in text:
#         if i == number:
#             n += 1
#         elif i == letter:
#             k += 1
#         # else:
#         #     return 'ERROR'
#     return f"count of {number}={n}\ncount of {letter}={k}"
# text = input('Enter text: ')
# number = input('Enteer number: ')
# letter = input('Enter letter: ')
# print(count_letters(text))

#6---------------------------------------------------------

# def finde(x,y):
#     if (x ==1 or x == -1) and (y == 1 or y == -1):
#         return 'Монетка где-то рядом'
#     else:
#         return 'Монетки в области нет'
# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# print(finde(x,y))


#7--------------------------------------------------------------

# def minimum(a,b):
#     return (a + b - abs(a - b)) / 2
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(minimum(a,b))

#8-----------------------------------------------------------------

# def divider(a,b):
#     div=[]
#     for i  in range(1,min(a,b)+1):
#         if a%i == 0 and b%i == 0:
#             div.append(i)
#     return max(div)
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(divider(a,b))

#9------------------------------------------------------------------
# import testfunc

# start_game = input('Start game? yes or no: ')
# if start_game == 'yes':
#     name = input('Enter your name: ') 
#     print(f'-----Hello {name}-----')

# while start_game != 'no':
    
#     testfunc.mainMenu()

#     start_game = input('Restart game? yes or no: ')

# print('-----Goodbye-----')



