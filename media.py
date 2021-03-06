import webbrowser

class Movie:
    """ Movie Class """
    def __init__(self, title, storyline, poster_image, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
