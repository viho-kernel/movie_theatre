Movie Theatre App - Project Notes 🎬
Project Overview
The Movie Theatre App is a simple console-based Python application that allows users to manage a list of movies. Users can add movies, list all movies, search for a specific movie by title, and quit the application. The project is designed to demonstrate basic programming concepts such as loops, conditionals, functions, and data structures in Python.
Key Features
Add a Movie:

Users can add a new movie by entering the title, director, and release year.
The movie is stored in a list as a dictionary with keys for title, director, and year.
List All Movies:

Users can view all the movies they’ve added in a simple list format.
If no movies have been added yet, the app will notify the user.
Find a Movie by Title:

Users can search for a movie by entering the title.
The search is case-insensitive, meaning the app will match titles regardless of capitalization.
If the movie is found, its details (title, director, year) are displayed. If not, the app will notify the user.
Quit the Application:

Users can quit the application by entering 'q'. A goodbye message is displayed before exiting.
Code Design and Structure
The movie data is stored as a list of dictionaries. Each dictionary represents a movie with its title, director, and release year.

The program runs in a while loop that keeps showing the menu until the user decides to quit by entering 'q'.

Menu Options:

'a': Prompts the user to add a new movie.
'l': Lists all the movies in the collection.
'f': Finds a specific movie by title.
'q': Quits the program.
The program provides user-friendly feedback for each action, such as confirming when a movie is added, notifying when a search result is found or not, and informing when no movies are in the list.
