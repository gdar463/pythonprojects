import random

def create_wordsearch(words):
    grid=[[random.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(20)]for _ in range(20)]
    print(grid)
    for row in grid:
        print(''.join(row))

    for word in words:
        x,y= random.randint(0,9), random.randint(0,9)
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])
        if direction == 'horizontal':
            for i,letter in enumerate(word):
                grid[y][x+i] = letter
        elif direction == 'vertical':
            for i,letter in enumerate(word):
                grid[y+i][x] = letter
        else:
            for i,letter in enumerate(word):
                grid[y+i][x+i] = letter

    for row in grid:
        print(''.join(row))

words=input("Enter words to include in the word search (separated by commas):").split(',')
create_wordsearch(words)
