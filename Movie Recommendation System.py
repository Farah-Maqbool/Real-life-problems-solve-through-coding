#Movie Recommendation System
"""Movie Recommendation System: Create a program that recommends movies based on user 
preferences. Use variables to store genre, rating, and release year. Write expressions to 
compare movies and suggest matches."""
genre=input("Genre (Movie): ").lower()

if genre=="movie":
    rating=input("Rating (eg *****): ")
    release_year=input("Release year: ")
    if rating=="*****" and release_year=="2015":
        print(f'The movie that matches your preferences is "The Martian"')
    elif rating=="***" and release_year=="2010":
        print(f'The movie that matches your preferences is "The Social Network"')
    elif rating=="****" and release_year=="2014":
        print(f'The movie that matches your preferences is "The Imitation Game"')
    else:
        print("Sorry, not a movie that matches your preferences.")
else:
    print(f"Here, you see options related to movies, not {genre}.")
