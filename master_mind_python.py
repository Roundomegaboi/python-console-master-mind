#mastermind
import random

#classes
class board:
    def __init__(self):
        #previous user guesses and hints stored as 2d lists
        self.board = [['-' for i in range(4)] for j in range(8)]
        self.hints = [['-' for i in range(4)] for j in range(8)]
        
        self.round = 0
        self.color_codes = {
                        1 : 'GRE',
                        2 : 'BLU',
                        3 : 'RED',
                        4 : 'PUR',
                        5 : 'BRO',
                        6 : 'BLA',
                        7 : 'ORA',
                        8 : 'YEL'
            }
        
        #randomly choose correct colors, only one of each color possible
        options = [value for value in self.color_codes.values()]
        self.correct = []
        for i in range(4):
            index = random.randint(0,len(options)-1)
            item = options.pop(index)
            self.correct.append(item)
            
        
    def display(self, show_unknown=False):
        long_dash = '-'*36
         
        #header 
        print(long_dash)
        print(' '*13+'MasterMind' +' '*13)
        print(long_dash)
        
        #parse and print board line by line
        for index, row in enumerate(self.board):
            board_nums = ''
            hints = ''
            for item in row:
                spaces = 5 if len(item) == 1 else 3
                board_nums += item
                board_nums += ' '*spaces
            
            for hint in self.hints[index]:
                hints += hint + ' '
                
            print(' '*8 + '|')
            print(hints + '|   ' + board_nums)
            print(long_dash)
        
        #footer
        if show_unknown:
            unknown =''
            for color in self.correct:
                unknown += f'{color}   '
            print(' '*8+ '|   '+unknown)
        else: 
            print(' '*8 + '|   ' + 'UNK   '*4)

    def update(self,colors):
        #update previous player guesses section
        for i in range(len((self.board[self.round]))):
            self.board[self.round][i] = self.color_codes[colors[i]]
            
        #update hints section
        for i in range(4):
            if self.correct[i] == self.color_codes[colors[i]]:
                self.hints[self.round][i] = '✓'
            
            elif self.color_codes[colors[i]] in self.correct:
                self.hints[self.round][i] = 'O'
                
            else:
                self.hints[self.round][i] = 'X'
        
        self.round += 1
        
    def check_victory(self, colors_num):
        if self.round > 7:
            return 0
        
        colors = []
        for color in colors_num:
            colors.append(self.color_codes[color])
            
        if colors == self.correct:
            return 1
        
        else:
            return 2
        
    
        
    
#main
game_board = board()
game = True
print('Welcome to Mastermind - press enter to start game!')
input()

while game:
    #print numbers corresponding to colors
    print('Enter the numbers of each color you select: ')
    for key, value in game_board.color_codes.items():
        print(f'{value}({key})')
        
    #collect user input
    user_colors = []
    for i in range(4):
        color = int(input(f'Enter number {i+1}: '))
        user_colors.append(color)
    
    
    game_board.update(user_colors)
    victory = game_board.check_victory(user_colors)
    
    #0 = loose
    if victory == 0:
        print('Ran out of guesses!')
        game_board.display(show_unknown=True)
        game = False
        continue
    
    #1 = user win
    elif victory == 1:
        print('You won!')
        game_board.display(show_unknown=True)
        game = False
        continue
    
    #2 = continue game
    else:
        print('Have another guess.')
        game_board.display()
        