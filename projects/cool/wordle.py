import random
import os
import time

os.system('clear')

word_list = open('wordle_list_2026.txt').read()
word_list = word_list.split('\n')

word_info = random.choice(word_list)
word_date = word_info[:-5]
word = word_info[-5:].lower()

for i in range(6):
    inp = input()
    while len(inp) != 5: 
        inp = input()

    for j in range(5):
        if inp[j] not in word:
            print('⬜', end='')
            continue
        elif inp[j] != word[j]:
            print('🟨', end='')
            continue
        else:
            print('🟩', end='')
            continue

    print()

    if inp == word:
        print('success!')
        print('tries:', i+1)
        break

print('word:',word)
print('date:',word_date)