import media
import fresh_tomatoes

# creating movie instances

twentyseven_dresses = media.Movie("27 Dresses",
						"After serving as a bridesmaid 27 times, a young woman"
						" wrestles with the idea of standing by her sister's "
						"side as her sibling marries the man she's secretly in"
						" love with.",
						"https://upload.wikimedia.org/wikipedia/en/4/48/Twenty"
						"_seven_dresses.jpg",
						"https://www.youtube.com/watch?v=VV1-pePln_I")

confessions_of_a_shopaholic = media.Movie("Confessions of a shopaholic",
						"A college grad lands a job as a financial journalist "
						"in New York City to support where she nurtures her "
						"shopping addiction and falls for a wealthy"
						" entrepreneur",
						"https://upload.wikimedia.org/wikipedia/en/1/10/Confes"
						"sions_of_a_Shopaholic.jpg",
						"https://www.youtube.com/watch?v=ZYYCSEV-i1Y")

kill_bill = media.Movie("Kill Bill: Volume 1", 
						"The Bride wakens from a four-year coma. The child she"
						" carried in her womb is gone. Now she must wreak veng"
						"eance on the team of assassins who betrayed her - a t"
						"eam she was once part of.",
						"https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_"
						"bill_vol_one_ver.jpg",
						"https://www.youtube.com/watch?v=ot6C1ZKyiME")

sister_act_one = media.Movie("Sister Act", 
						"When a worldly singer witnesses a mob crime, the poli"
						"ce hide her as a nun in a traditional convent where s"
						"he has trouble fitting in.",
						"https://upload.wikimedia.org/wikipedia/en/a/a3/Sister"
						"_Act_film_poster.jpg",
						"https://www.youtube.com/watch?v=I-Yi-WGG-6c")

love_actually = media.Movie("Love Actually", 
						"Follows the lives of eight very different couples in "
						"dealing with their love lives in various loosely inte"
						"rrelated tales all set during a frantic month before "
						"Christmas in London, England.",
						"https://upload.wikimedia.org/wikipedia/en/e/eb/Love_A"
						"ctually_movie.jpg",
						"https://www.youtube.com/watch?v=cYCkFTyADJ0")

#list for movies
movies = [twentyseven_dresses, confessions_of_a_shopaholic, kill_bill, 
		sister_act_one, love_actually]

fresh_tomatoes.open_movies_page(movies)
