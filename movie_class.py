import webbrowser

# Define the Movie class with the properties of title, storyline, image, trailer and director.

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.director = movie_director

    # Define the show trailer method within the Movie class.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

