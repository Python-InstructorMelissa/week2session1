import random

# from <file name> import <function name>
# List of players each index is a dictionary of a player

players = [
    {"name": "Melissa", "skillLevel": 1, "health": 100},
    {"name": "Steve", "skillLevel": 2, "health": 100},
    {"name": "Rod", "skillLevel": 1, "health": 100},
    {"name": "Eion", "skillLevel": 4, "health": 100}
]

# print("print whole initial list: ", players)
# print("print 1 player: ", players[0]['name'])

playerNames = []
playerSkills = []
def printPlayers():
    for player in range(len(players)):
        # print("each iteration of player: ", players[player]['name'])
        p = players[player]['name']
        skill = players[player]['skillLevel']
        # print("print name: ", p)
        # print(f"print all player names {p}")
        # print(f"alternate print of names {players[player]['name']}")
        playerNames.append(p)
        playerSkills.append(skill)
    print(f"Print list of players {playerNames} \nPrint list of their skills {playerSkills}")

printPlayers()

