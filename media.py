import webbrowser

#class definition for Movie

class Movie():
	"This class provides a way to store movies"""
	
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	
	#initialises  class 
	def __init__(self, move_title, movie_storyline, poster_image, trailer_youtube):
		self.title = move_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)