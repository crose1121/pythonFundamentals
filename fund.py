def add(a,b):
    x = a+b
    return x

print(add(2,3))

def say_hi(arr):
    for n in arr:
        if type(n)==str:
            print(f"Hi {n}")


heroes = ["Iron Man", "Hulk", "Wonder Woman", "Thor"]
villains = ["Thanos", "Joker", "Ultron",["Marvel", "DC"]]


say_hi(heroes)
say_hi(villains)


for v in villains[3]:
    print(v)

for i in range(0,len(heroes)):
    print(i,heroes[i])

for villain in villains:
    print(villain)

for i in range(5,11):
    print(i)

for i in range(5,0,-2):
    print(i)


countdown = 10
while countdown > 0:
    print(countdown)
    countdown-=1
print("Happy New Year!")



ironman = {
    "name":"Tony Stark",
    "bday": "5/29/1970",
    "weight": 160,
    "powers": {
        "power1": "Genius",
        "power2": "Master Engineer"
    },
    "traits":["cocky","nuts"]
}

for i in ironman:
    print(ironman[i])

for i in ironman["powers"]:
    print(i,ironman["powers"][i])

print(ironman["name"])
ironman["age"] = 51
print(ironman)
print(ironman["powers"]["power2"])
print(ironman["traits"][0])


heroes = ["Iron Man", "Hulk", "Wonder Woman", "Thor"]
villains = ["Thanos", "Joker", "Ultron",["Marvel", "DC"]]
empty = []

print(heroes)
print(villains)
print(villains[2])
print(villains[3][1])
heroes.append("Spider Man")
print(heroes)

from random import randint
print(randint(1,6))



likes_bbq = True
likes_fruit = False
weight = 160.5
iq = 300
name = "Corey"
age = "15"


if likes_bbq:
    weight += 10
    print(name + " weighs " + str(weight) + "lbs")

if likes_bbq and weight > 160:
    weight += 10
    print(f"I'm getting fat :( my weight is {weight}")

elif likes_fruit or iq>100:
    weight -= 10
    print(weight)

else:
    print(weight)




question = "Why did the chicken go to the seance?"
punchline = "\nTo get the other side!"

print(question, punchline)

#comment with a hashtag

'''
DocString with triple ' above and below
'''

