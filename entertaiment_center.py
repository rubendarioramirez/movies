import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A Story of a boy and his toy that comes to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar", "A marine on an Alien plant", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
school_of_rock = media.Movie("School of Rock", "A guy that plays the guitar", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
somethingelse = media.Movie("Something else", "A guy that plays the guitar", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
another_movie = media.Movie("Another Movie", "A guy that plays the guitar", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")

movies = [toy_story, avatar, school_of_rock, somethingelse, another_movie]
fresh_tomatoes.open_movies_page(movies)


#avatar.show_trailer()

