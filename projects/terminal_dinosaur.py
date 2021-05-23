import time
import os
import random
os.system('clear')
# 🟥🟧🟨🟩🟦🟪⬛️⬜️🟫

# # y_ = random.randrange(5)
# for y_ in range(5):
#     for x_ in range(19,0,-1):
#         for y in range(5):
#             for x in range(20):
#                 if x == x_ and y == y_:
#                     print('🟥', end = '')
#                 else:
#                     print('⬜️', end = '')
#             print()
#         time.sleep(.05)
#         os.system('clear')

for y in range(5):
    for x in range(5):
        print('⬜️', end = '')
    print()
print(input())