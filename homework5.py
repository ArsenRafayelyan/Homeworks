#173---------------------------------------------------------

# def summ():
#     number = input('Enter number: ')
#     if number == '':
#         return 0.0
#     else:
#         return int(number) + summ()
# print(summ())

#174---------------------------------------------------------------------

    
# def divider(a,b):
    
#     if b == 0:
#         return a
#     else:
#         c = a%b
#         return divider(b,c)
# a = int(input('Enter a: ')) 
# b = int(input('Enter b: ')) 
# print(divider(a,b))    

#175--------------------------------------------------------------------------

# def binar(number,a = ''):
#     if number == 1:
#         return f'{number}{a[::-1]}'
#     else:
#         return binar(number//2,a+str(number%2))
# number = int(input('Enter number: '))
# print(binar(number))

#176------------------------------------------------------------------

# def code(word):
#     shifr = {
# 'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel',
# 'I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec',
# 'R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu'
# }
#     if word == '':
#         return ''
#     else:
#         print(shifr[word[0]])
#         x = word[1:len(word)]
#         return code(x)
    

# word = input('Enter word: ').upper()
# print(code(word))

#177-------------------------------------------------------------------------

# rim1 = {'IX':9,'VIII'}

# rim = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

#178------------------------------------------------------------------------

# def polidrom(word):
#     if len(word) <= 1:
#         return 'Polidrom'
#     if word[0] != word[-1]:
#             return 'NO polidrom'
#     else:
#         return polidrom(word[1:-1])
# word =input('Enter word: ')
# print(polidrom(word))


#179---------------------------------------------------------------------------

# def squer(n,gues):
    
#     if (gues**2) -n < 10**-12:
#         return gues
#     else:
        
#         return squer(n,(gues + n / gues)/2)
# n = int(input('Enter n: '))
# gues = n/2
# print(squer(n,gues))


#180-----------------------------------------------------------------------------


# def distanc(s,t):
#     if len(s) == 0:
#         return len(t)
#     if len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[len(s)-1] != t[len(t)-1]:
#             cost = 1
#         d1 = distanc(s[0:-1],t) +1
#         d2 = distanc(s,t[0:-1]) +1
#         d3 = distanc(s[0:-1],t[0:-1]) +cost
#     return min(d1,d2,d3)
# s = input('Enter word s: ')
# t = input('Enter word t: ')
# print(distanc(s,t))



#184----------------------------------------------------------------------------


# def func(mylist):
    
#     if mylist == []:
#         return []
#     if isinstance(mylist[0],list):
#         return func(mylist[0]) + func(mylist[1:])
#     else:
#         return [mylist[0]] + func(mylist[1:])
# mylist = [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]
# print(func(mylist))



