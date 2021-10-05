# create a list has the players
import random

players = [
    {"name": "Jill", "1": 0, "2": 0, "3": 0}, # index 0
    {"name": "Phoenix", "1": 0, "2": 0, "3": 0}, # index 1
    {"name": "French", "1": 0, "2": 0, "3": 0}, # index 2
    {"name": "Bob", "1": 0, "2": 0, "3": 0}, # index 3
]

# keys = players[0].keys()
# values = players[0].values()
# pairs = players[0].items()

# print("Keys", keys)
# print("Values", values)
# print("Items", pairs)

def make_rolls():
    for i in range(len(players)): # Loop through the players list
        for p in range(1, 4): # Looop through each dictionary and target the keys 1, 2 and 3 for each one 
            players[i][str(p)] = random.randint(1,100) # Set the values of those keys to a random no=umber 1-100
            # Setting a low range causes recursion timeout
        print(players[i].items()) # Display the dictionaries with the new values
    check_winner()



def check_winner():
    winner = ""
    high = 0
    for player in players:
        for key, value in player.items():
            # looping through each dictionary, we only want to check the value if its a number
            if type(value) is int:
                if value > high: # if the current value in the dictionary is higher then the last recorded
                    high = value # set the highest value equal to the current value
                    winner = player['name'] # Set the winner to the current players name in the loop
                elif value == high: # If there are two winners at any point reroll
                    make_rolls()
    print(f"{winner} wins - {high}") # Display the winner



make_rolls()
