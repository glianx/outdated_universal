#St Petersburg coin toss - https://en.wikipedia.org/wiki/St._Petersburg_paradox 
#A coin is flipped until we get heads. 
#
import random
rewards = []
flipcount = 0

def flip():
    global flipcount
    coinflip = random.randrange(2)
    print(coinflip)
    flipcount += 1
    if coinflip == 0: #tails
        flip()
    elif coinflip == 1: #heads
        print(f'total flips = {flipcount}, reward = {2**flipcount}')
        rewards.append(2**flipcount)
        flipcount = 0

attempts = 10**4
for x in range(attempts):
    flip()

print(rewards)
print(f'total rewards after {attempts} attempts = ${sum(rewards)}')
print(f'expected value = {sum(rewards)}/{attempts} = ${sum(rewards)/attempts}')