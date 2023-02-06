#2-------------------------------------------------------

# student = {'1':5,'2':8,'3':9,'4':8,'5':7,'6':8,'7':8,'8':9,'9':4,'10':7}
# summ = 0
# count = 0
# for i in student:
#     summ += student[i]
#     count += 1
# print(summ/count)


#3------------------------------------------------------------------------

# student = {'1':5,'2':8,'3':9,'4':8,'5':7,'6':8,'7':8,'8':9,'9':4,'10':7}
# good = {i:student[i] for i in sorted(student,key=student.get)[:5]}
# bad = {i:student[i] for i in sorted(student,key=student.get,reverse=True)[:5]}
# print(good)
# print(bad)

#4-------------------------------------------------------------------------

# student = {'1':5,'2':3,'3':9,'4':1,'5':7,'6':4,'7':8,'8':9,'9':4,'10':7}
# newdict = {}
# for i in student:
#     if student[i] >= 5:
#         print(i,student[i])

#5-----------------------------------------------------------------
# student = {'1':5,'2':3,'3':9,'4':1,'5':7,'6':4,'7':8,'8':9,'9':4,'10':7}
# newdict = {}
# for i in student:
#     if student[i] < 5:
#         print(i,student[i])


#6--------------------------------------------------------------------
# a = input('Enter noute: ')
# mydict = {'mac':10,
#           'hp':9,
#           'lenovo':8
# }

# print(a in mydict)

#7-------------------------------------------------------------------------

# s = 'a,2,b,5,c,8,a,4,e,11'

# items = s.split(',')
# d = {}
# for i in range(0, len(items), 2):
#     key = items[i]
#     value = int(items[i+1])
#     if key in d:
#         d[key] += value
#     else:
#         d[key] = value
    
# print(d)

    
    
#8------------------------------------------------------------

# word = "hello, world"

# d = {}
# for i in word:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)           

#9--------------------------------------------------------------

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []
# for i in old_list:
#     if i not in new_list:
#         new_list.append(i)
# # print(new_list)

# #136-----------------------------------------------------------------
# myvalu = [2,6,4,8,9,3]
# mydict = {'a':2,'b':7,'c':4,'d':7,'e':7}
# newdict = {}

# for i,j in mydict.items():
#     if j in myvalu:
#         newdict[i] = [j]
# print(newdict)

# #137----------------------------------------------------------------
# import random
# list1 = [0,0,0,0,0,0,0,0,0,0,0]
# list2 =[2,3,4,5,6,7,8,9,10,11,12]
# for i in range(1000):
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     list1[a+b-2]+= 1
# j = 2
# for i in list1:
#     print(j,round(i/1000*100,2),'%')
#     j+=1

#138----------------------------------------------------
# letters = {'1':'.,?!:','2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz','0':' '}
# word = (input("Введите фразу: ")).lower()
# for i in word:    
#     for j in letters:  
#         if i in letters[j]:    
#             for x in letters[j]:
#                 if x == i:
#                     print(j, end='') 
#                     break
#                 else:
#                     print(j, end='')

#139------------------------------------------------------------------

# morze = {'A': '.-','B':'-...',
#          'C': '-.-.', 'D': '-..', 'E': '.',
#          'F': '..-.', 'G': '--.', 'H': '....',
#          'I': '..', 'J': '.---', 'K': '-.-',
#          'L': '.-..', 'M': '--', 'N': '-.',
#          'O': '---', 'P': '.--.', 'Q': '--.-',
#          'R': '.-.', 'S': '...', 'T': '-',
#          'U': '..-', 'V': '...-', 'W': '.--',
#          'X': '-..-', 'Y': '-.--', 'Z': '--..',
#          '1': '.----', '2': '..---', '3': '...--',
#          '4': '....-', '5': '.....', '6': '-....',
#          '7': '--...', '8': '---..', '9': '----.',
#          '0': '-----', ', ': '--..--', '.': '.-.-.-',
#          '?': '..--..', '/': '-..-.', '-': '-....-',
#          '(': '-.--.', ')': '-.--.-'}
# text = input('Enter word: ').upper().split()
# for i in text:
#     for j in i:
#         print(" ".join([morze[j]]))


#140--------------------------------------------------------------------------

# index = {'Ньюфаундленд':'A',
# 'Новая Шотландия':'B',
# 'Остров Принца Эдуарда':'C',
# 'Нью-Брансуик':'E',
# 'Квебек':'G,H,J',
# 'Онтарио':'K,L,M,N,P',
# 'Манитоба':'R',
# 'Саскачеван':'S',
# 'Альберта':'T',
# 'Британская Колумбия':'V',
# 'Нунавут':'X',
# 'Северо-Западные территории':'X',
# 'Юкон':'Y',
# }
# text = input('Enter index: ').upper()
# for i in index:
#     if text[0] in index[i] and text[1] != '0':
#             print('город: ',i)
#     elif text[0] in index[i] and text[1] == '0':
#           print('сельской местности: ',i)

#141---------------------------------------------------------------------------

# ones = {
#     0: '',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine'
# }

# teens = {
#     10: 'ten',
#     11: 'eleven',
#     12: 'twelve',
#     13: 'thirteen',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'nineteen'
# }

# tens = {
#     2: 'twenty',
#     3: 'thirty',
#     4: 'forty',
#     5: 'fifty',
#     6: 'sixty',
#     7: 'seventy',
#     8: 'eighty',
#     9: 'ninety'
# }

# number = int(input("Enter a number: "))
# result = []

# if number // 100 > 0:
#     result.append(ones[number // 100] + " hundred")
#     number = number % 100

# if number // 10 >= 2:
#     result.append(tens[number // 10])
#     number = number % 10

# if number // 10 == 1:
#     result.append(teens[number])
#     number = 0

# if number > 0:
#     result.append(ones[number])

# print(" ".join(result))

#142----------------------------------------------------------
# word = input('Enter a word: ')
# unique_chars = {}
# for i in word:
#   if i not in unique_chars:
#     unique_chars[i] = 1
# print('count = ', len(unique_chars))


#143----------------------------------------------------------

# word1 = input('Enter word1:')
# word2 = input('Enter word2:')
# if sorted(word1) == sorted(word2):
#     print("The words are anagrams.")
# else:
#     print("The words are not anagrams.")

#144-----------------------------------------------------------

# text1 = input('Enter text1:').lower().replace(' ','')
# text2 = input('Enter text2:').lower().replace(' ','')
# if sorted(text1) == sorted(text2):
#     print("The text are anagrams.")
# else:
#     print("The text are not anagrams.")

#145-------------------------------------------------------------

# score = {
#     1:'A, E, I, L, N, O, R, S, T , U',
#     2:'D,G',
#     3:'B, C, M , P',
#     4:'F, H, V, W , Y',
#     5:'K',
#     8:'J,X',
#     10:'Q,Z'
# }
# summ = 0
# word = input('Enter word: ').upper()
# for i in score:
#     for j in word:
#         if j in score[i]:
#             summ+=i
# print('Your score = ',summ)

#146---------------------------------------------------------------

# import random

# cart = {
#     'B':[],
#     'I':[],
#     'N':[],
#     'G':[],
#     'O':[]
# }
# res = 1
# for i in cart:
    
#     while len(cart[i]) != 5:
#         b = random.randint(res,res+14)
#         if b not in cart[i]:
#             cart[i].append(b)
#     res += 15

# for i in cart:
#     print(i,end='    ')
# print("")
# print("")
# for i in cart:
#     for j in cart[i]:
#         if j<10:
#             print(j,end="    ")
#         else:
#             print(j,end="   ")
#     print("")
    
#---------------------------------------------------
