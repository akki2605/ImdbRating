import imdb
from tabulate import tabulate

Imdb = imdb.IMDb()


def getRatings():

    # taking input from user
    getMovieName = input("Enter Movie name : \n")

    # getting the movieID and movieName according to the input
    movieName = Imdb.search_movie(getMovieName)


# Printing the movieId and movieName output in a tabluate from....
    table = [[movie.movieID, str(movie)] for movie in movieName]
    headers = ["Movie ID", "Name"]
    print(tabulate(table, headers, tablefmt="psql"))

    if(movieName):

        try:
            # input for the movieID
            getMovieCode = input(
                "Enter the Movie ID for the movie you looking for: \n")

            # extract data of the movie according to the movieCode
            query = Imdb.get_movie(getMovieCode)

            # Printing the movie as well as its IMDB Rating
            print("Ratings for the Movie < {} > is: {}".format(
                query.data["title"], query.data["rating"]))

        except Exception as ee:
            print("Wrong Movie ID entered")

    # If the Movie entered is not in the data
    else:
        print("Movie name out of range")


getRatings()
