""" This is an example program that creates a list 'alist' of Movie objects.
The class Movie is implemented in file 'media'. Import media as the first
statement. Then import the 'fresh_tomatoes' implementation that was downloaded.
Provided by course author. Then call the function that creates the web page
"""
import media
import fresh_tomatoes

#def createMovieObj(aTitle,aDesc,aPosterURL,aYouTubeTrailerURL):
#""" Retuns the Movie object/instance """
#    return( media.Movie(aTitle,aDesc,aPosterURL,aYouTubeTrailerURL)

aMovieList=[    #START :Initialize alist with 7 movies contents 
media.Movie(
    "Toy Story",
    "A story of boy and this toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
            ),
media.Movie(
    "Avatar",
    "About a marine on alien land",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
            ),
media.Movie(
    "Lion King",
    "Not sure if this needs Introduction",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
              ),
media.Movie(
    "Ocean 13",
    "Danny Ocean's friend Reuben goes after Willy Bank to take revenge",
    "http://www.impawards.com/2007/posters/oceans_thirteen.jpg",
    "https://www.youtube.com/watch?v=L-EyG12LxME"
            ),
media.Movie(
    "Ocean's 14",
    "Ocean series 14 not: Distant confusion",
    "http://cdn1-www.afterellen.com/assets/uploads/images/Ocean%27s%2014.jpg",
    "https://www.youtube.com/watch?v=rpHR-y_woRw"
          ),
media.Movie(
    "Ocean 12",
    "American comedy heist film, the first sequel to 2001's Ocean's Eleven.",
    "http://www.impawards.com/2004/posters/oceans_twelve.jpg",
    "https://www.youtube.com/watch?v=Ze4WPu2kHus"
            ),
media.Movie(
    "Ocean 11",
    "Centered on a series of Las Vegas casino robberies",
    "http://www.digitallyobsessed.com/cover_art1/oceans11-2001.jpg",
    "https://www.youtube.com/watch?v=Ze4WPu2kHus"
            )                  
]       #END:Initialize alist with 7 movies contents 

""" Call the function that creates the page dynamically """
fresh_tomatoes.open_movies_page(aMovieList)

