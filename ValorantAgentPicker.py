from random import randint

# all current agents as of October 18th, 2022
AGENTS = ["Brimstone", "Viper", "Omen", "Killjoy", "Cypher", "Sova", 
          "Sage", "Phoenix", "Jett", "Reyna", "Raze", "Breach", 
          "Skye", "Yoru", "Astra", "KAY/O", "Chamber", "Neon", 
          "Fade", "Harbor"]

# function to give a random agent in AGENTS
def generator():
    length = len(AGENTS) - 1
    agent = AGENTS[randint(0, length)]
    return agent

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
# our roster of agents
roster = []

# our first agent, we don't need to check if it's unique since it's the only one
roster.append(generator())
playercount = int(response)
x = 1
while(x < playercount):
    unique = False
    while not unique:
        nextagent = generator()
        for agent in roster:
            if nextagent == agent:
                nextagent = generator()
                break
        unique = True
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
