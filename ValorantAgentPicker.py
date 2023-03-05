from random import randint
import os

if not os.path.exists("./agents.txt"):
    print("WOAH THERE!!")
    print("You're trying to run this program without the agents file!")
    print("Please make sure there's a file called \"agents\" in the main directory.")
    swaws = input()
    exit()

# function to give a random agent in AGENTS
def generator():
    length = len(AGENTS) - 1
    agent = AGENTS[randint(0, length)]
    return agent

# reads the agents file 
def readAgentsFile(array, file):
    with open(file, "r") as file:
        for line in file:
            if '#' not in line:
                array.append(line.strip())

# array that will contain the list of agents
AGENTS = []

readAgentsFile(AGENTS, "./agents.txt")

hasPicked = False
playercount = 0

# get user input on how many players there are
while not hasPicked:
    print("How many players are there?")
    response = input()

    try:
        playercount = int(response)
    except:
        print("That's not a number! Try again!\n\n\n")
        continue
    else:
        playercount = int(response)
    
    if playercount > 5 or playercount < 1:
        print("That's an invalid amount! Try again!\n\n\n")
        continue
    else:
        hasPicked = True

if int(response) > len(AGENTS):
    print("HEY! You gave too many players for the amount of blacklisted agents! \n\nEiter change playercount or whitelist more agents!")
    swaws = input()
    exit()

# our roster of agents
roster = []

# our first agent, we don't need to check if it's unique since it's the only one
roster.append(generator())
playercount = int(response)
x = 1
while(x < playercount):
    nextagent = generator()
    if nextagent not in roster:
        roster.append(nextagent)
        x += 1

# roster after all agents are picked
print("\n\n\nThe roster is ready!")

for agent in roster:
    playernum = roster.index(agent) + 1

    print("Player " + str(playernum) + ": " + agent)



print("Good luck! (You might need it...)")
print("Or you can try to reroll by pressing 'R'! Press anything else to quit.")

response = input()
response.lower()

# if the user has no objections to the rng
if response != "r":
    exit()

# checks that number the user gave is proper (all numbers are between 1-playercount, and that it's an actual number)
hasPicked = False
while not hasPicked:
    print("\n\n\nType which players need a reroll\nFor example, if players 1 and 3 need a reroll, type \"13\"")
    response = input()
    reroll = []
    for char in response:
        try:
            int(char)
        except:
            print("That's not a number! Try again!\n\n\n")
            hasPicked = False
            continue
        else:
            responsetonum = int(char)
            reroll.append(responsetonum)

    for num in reroll:
        if num > playercount or num < 1:
            print("That's not a player! Try again!\n\n\n")
            hasPicked = False
            break
        else:
            hasPicked = True

# somewhat similar to what happened above, but rather than appending, just changes the specific players instead
for num in reroll:
    agent = generator()
    unique = False
    while not unique:
        nextagent = generator()
        for agent in roster:
            if nextagent == agent:
                nextagent = generator()
                break
        unique = True 
    roster[num-1] = nextagent

# exact same as when the rost was first done
print("\n\n\nThe roster is ready!")

for agent in roster:
    playernum = roster.index(agent) + 1

    print("Player " + str(playernum) + ": " + agent)


print("Good luck! (You might need it...)")
ass = input()