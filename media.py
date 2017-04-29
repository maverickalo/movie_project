##IMPORT THE WEBBROWSER CLASS

import webbrowser

##DEFINE WHAT WILL MAKE UP THE MOVIE CLASS AND HOW IT WILL BE ORGANIZED BELOW

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

##BELOW DEFINES THE SHOW_TRAILER METHOD ALLOWING THE YOUTUBE LINK TO OPEN IN THE SAME WINDOW

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
