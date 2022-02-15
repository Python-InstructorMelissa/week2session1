movies = [
    {
        'id': 1,
        'title': "Back to the Future",
        'year': 1984,
        'actors': [
            {'firstName': "Michael J", 'lastName': "Fox"},
            {"firstName": "Christopher", 'lastName': "Lloyd"}
        ],
        'genre': "Syfy Drama"
    },
    {
        'id': 2,
        "title": 'Rambo 1st blood',
        'year': 1982,
        'actors': [
            {'firstName': "Sylvester", "lastName": "Stallone"},
            {'firstName': "David", 'lastName': "Caruso"},
            {'firstName': 'Brian', 'lastName': 'Denning'}
        ],
        'genre': 'Action'
    },
    {
        'id': 3,
        'title': 'Teen Wolf',
        'year': 1985,
        'actors': [
            {'firstName': "Susan", 'lastName': "Ursitti"},
            {'firstName': "Michael J", 'lastName': "Fox"}
        ],
        'genre': "Syfy Drama"
    }
]

# Use a for loop when you expect their to be more than 1 result and don't use one if you know it will only return 1


# Create a function that prints back the whole list of movies
def printList(x): # function taking 1 parameter
    print("Whole list: ", x) # print statement to print back what is being passed in

# printList(movies)  # activating the function and passing in the desired list or data set

# The functions will be called through the front end or a form typically on the webpage

# Print back just the titles of all the movies contained in the list
def printTitles(x):
    for i in x: # because we know we might get more than 1 result we use a for loop 
        print("All the movie titles: ", i['title']) # Because we just want the movie titles we say that for each loop through just print back the title

# printTitles(movies)

# Print the list of actors for 1 movie
def movieActors(x):
    print("The selected movies actor list: ", x['actors']) # Here because we will use the calling of the function to narrow down what dictionary to look in we can say just print back the list of actors

# movieActors(movies[0]) # Here we are calling just 1 instance from our data set
# movieActors(movies[1])
# movieActors(movies[2])

# Check to see if a given movie instance has a specific actor in it
def checkActor(x, y):
    for i in x: # going to loop through the list of actors in the chosen movie
        if i['firstName'] == y: # checks each actor's first name against the chosen name and runs these instructions if true
            print(y, "is in this movie")  # if true will print the actors name
            return # because we don't need to keep checking the list of actors this will stop the loop
        else: # this will only run if the above is false
            print("Sorry", y, "isn't in this movie") # this will print for each actor that is in the loop where the if statement failed to stop the function

# checkActor(movies[2]['actors'], "Michael J") # activating function by passing in 1 movie and just it's list of actors and also a name for an actor to check


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# x[1] = [15,8,9] # an ok way to change the 10 to 15 but if it is a long list of numbers this would not be optimal
print(x)
x[1][0] = 15 # 9/10 times you will be able to get the id or index of what you want to edit so this is the best way to change the 10 to 15
print(x)
print("Kobe's first name only: ", sports_directory['basketball'][0])