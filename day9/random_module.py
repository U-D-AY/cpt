# random - genrate numbers ,random choices
# randint

import random as rn

# random.randint() // always b/w 0 & 1
print(f"Random number(randint) from 10 to 50: {rn.randint(10,50)}")

# random.random()
print(f"random number(random) from 0 to 1: {rn.random()}")

# random.uniform()
print(f"random number(uniform) from 1-100: {rn.uniform(1,100)}")

# random.choice()
aninames = ['Luffy', 'Zoro', 'Sanji', "brook",'jin rancandle','Luna','naruto','itachi']
print(f"Random choice from list: {rn.choice(aninames)}")

# random.choices()
print(f"Random choice from list: {rn.choices(aninames,k=2)}")

# random.sample()
print(f"Random choice from list: {rn.sample(aninames,3)}")

#random.shuffle()
print(f"Before Shuffle, list: {aninames}")
rn.shuffle(aninames)
print(f"After Shuffled list: {aninames}")

rn.seed(66)
print(rn.randint(1,100))