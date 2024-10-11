movies = []  # This will hold all the movies.

_input_menu = ''

while _input_menu != 'q':
    print("Hello! Welcome to the Movie Theatre")
    print('Menu!')
    _input_menu = input("Enter 'a' to add a movie, \n'l' to see your movies, \n'f' to find a movie by title, \nor 'q' to quit:\n ")

    if _input_menu == "a":
        # Adding a movie
        title = input("Enter the movie title: ")
        director = input("Enter the movie director: ")
        year = input("Enter the movie release year: ")

        movies.append(
            {
                'title': title,
                'director': director,
                'year': year
            }
        )
        print(f'Movie "{title}" added successfully!')
        print("Current movie list:", movies)  # Debug statement to show current list of movies

    elif _input_menu == "l":
        # List all movies
        if movies:
            print("\nYour movies:")
            for item in movies:
                print(f"Title: {item['title']}, Director: {item['director']}, Year: {item['year']}")
        else:
            print("\nNo Movies Found!")

    elif _input_menu == 'f':
        # Searching for a movie
        search_title = input("Enter the movie title you're searching for: ").lower()

        # Iterate over the list of movies
        for movie in movies:
            if movie['title'].lower() == search_title:
                print(f"Movie '{movie['title']}' found! Directed by {movie['director']} released in the year {movie['year']}")
                break
        else:
            print(f"Movie '{search_title}' is not found.")

    elif _input_menu == 'q':
        print("Goodbye!")

    else:
        print("Invalid option. Please try again later!")
