# def suum (num:list) ->int:
#     summ = 0
#     for i in num:
#         summ += i
#     return summ


# def maximum(num:list)->int:
#     m = None
#     for i in num:
#         if m is None or m < i:
#             m = i
#     return m
    
# def minimum (num:list)->int:
#     n = None
#     for i in num:
#         if n is None or i <n:
#             n = i
#     return n

#-------------------------------------------------------

# def rock_paper_scissors():
#     import random
#     user = input('Your step rock,paper or scissors:')
#     step = ['rock','paper','scissors']
#     pc = random.choice(step)
#     if pc == step[0] and user == step[1]:
#         return 'You win'
#     elif pc == step[0] and user == step[2]:
#         return 'Pc win'
#     elif pc == step[1] and user == step[0]:
#         return 'Pc win'
#     elif pc == step[1] and user == step[2]:
#         return 'You win'
#     elif pc == step[2] and user == step[0]:
#         return 'You win'
#     elif pc == step[2] and user == step[1]:
#         return 'Pc win'
#     else:
#         return 'PC = You'
        
# def guess_the_number():
#     your_number = int(input('Enter number 1-10: '))
#     import random
#     pc_number = random.randint(1,10)
#     if pc_number == your_number:
#         return 'You win'
#     else:
#         return 'Pc win'

# #-----------------------------------------------------------------------------

# def mainMenu():
#     game = input('Choice game: 1.rock_paper_scissors or 2.guess_the_number: ')
#     if game == '1':
#         print(rock_paper_scissors())
#     elif game == '2':
#         print(guess_the_number())
#     else:
#         print('NO game:')




