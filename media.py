import webbrowser
class Movie():
    """ The Class provides a container kind of class for movies.

        Each instance of this object will need the following 4 data to create
        an object.
            *amoveTitle : This is a string, a title of move. Example: Lion King
            *amovieStoryline: This is a short description of the movie
            *aposterImage: A URL link tot he poster for this movie.
                       example:"https://www.seple.com/Avatar-Teaser-Poster.jpg"
            *aYoutubeTrailer: A trailer URL for this movie
                    example:https://www.youtube.com/watch?v=L-EyG12LxME"
    """
    def __init__(self,amovieTitle,amovieStoryline,aposterImage,aYoutubeTrailer):
        """ A Simple and only constructor with 4 args as described in __doc__"""
        self.title= amovieTitle
        self.storyline=amovieStoryline
        self.poster_image_url=aposterImage
        self.trailer_youtube_url = aYoutubeTrailer
        
        
    def show_trailer(self):
        """Simply open the browser and run it in a webpage of default """
        aHandler=webbrowser.open(self.trailer_youtube_url)
        





   
