import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A Story of a boy and his toy that comes to life", "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an Alien plant", "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
school_of_rock = media.Movie("School of Rock", "A guy that plays the guitar", "http://www.gamerfocus.co/wp-content/uploads/2014/10/School-of-rock.jpg","https://www.youtube.com/watch?v=5afGGGsxvEA")


movies = [toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)

