import media
import fresh_tomatoes

the_secret_life_of_pets = media.Movie("The Secret Life of Pets",
                  "A terrier named Max's quiet life is upended when his owner takes in Duke, a stray whom Max instantly dislikes.",
                  "http://ia.media-imdb.com/images/M/MV5BMjIzMzA1OTkzNV5BMl5BanBnXkFtZTgwODE3MjM4NzE@._V1_.jpg",
                  "https://www.youtube.com/watch?v=UZJVc_JTI_w")

#print(fay.storyline)
#fay.show_trailer()
deadpool = media.Movie("Deadpool",
                   "A former Special Forces operative turned mercenary is subjected to a rogue experiment that leaves him with accelerated healing powers, adopting the alter ego Deadpool.",
                   "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg", 
                   "https://www.youtube.com/watch?v=9vN6DHB6bJc")

independence_day_resurgence = media.Movie("Independence Day: Resurgence",
                   "Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?", 
                   "http://ia.media-imdb.com/images/M/MV5BMjIyMTg5MTg4OV5BMl5BanBnXkFtZTgwMzkzMjY5NzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", 
                   "hhttps://www.youtube.com/watch?v=RfJgT89hEME")

movies = [the_secret_life_of_pets, deadpool, independence_day_resurgence]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__module__)
