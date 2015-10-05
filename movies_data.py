import movie_spot  #import movie_spot to run movie_spot.open_movies_page() below.
import movie_class #import movie_class contents to retrieve the Movie class

#create multiple instances of the Movie class

gladiator = movie_class.Movie("Gladiator",
                             "The epic story of the revenge of a gladiator, who ultimately defied and overthrew a corrupt emperor.",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",
                             "https://www.youtube.com/watch?v=IvTT29cavKo",
                             "Ridley Scott")

inception = movie_class.Movie("Inception",
                             "An exceptional team of experts work to implant an idea into the mind of a corporate CEO.",
                             "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                             "https://www.youtube.com/watch?v=8hP9D6kZseM",
                             "Christopher Nolan")

momento = movie_class.Movie("Momento",
                             "A man suffering with severe short term amnesia implements a system to track down and hunt the murderer of his wife.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                             "https://www.youtube.com/watch?v=0vS0E9bBSL0",
                             "Christopher Nolan")

the_dark_knight_rises = movie_class.Movie("The Dark Knight Rises",
                             "Bruce Wayne returns for the spectacular finale of the Batman trilogy.",
                             "http://img05.deviantart.net/9b39/i/2012/169/6/8/the_dark_knight_rises_by_cetosc-d497okc.jpg",
                             "https://www.youtube.com/watch?v=g8evyE9TuYk",
                             "Christopher Nolan")

interstellar = movie_class.Movie("Interstellar",
                             "A team of experts journey through a wormhole, taking a leap through space and time, in an effort to save humanity.",
                             "http://www.filmosophie.com/wp-content/uploads/2014/10/interstellar-poster.jpg",
                             "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                             "Christopher Nolan")

guardians_of_the_galaxy = movie_class.Movie("Guardians of the Galaxy",
                             "An unlikely band of companions join forces to save the galaxy in this hilarious Marvel epic.",
                             "http://blogs-images.forbes.com/markhughes/files/2014/07/Guardians-of-the-Galaxy-2-1308x1940.jpg",
                             "https://www.youtube.com/watch?v=B16Bo47KS2g",
                             "James Gunn")

the_wolf_of_wall_street = movie_class.Movie("The Wolf of Wall Street",
                             "Dark comedy based on the true story of the dramatic rise and fall of Jordan Belfort throughout Wall Street.",
                             "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                             "https://www.youtube.com/watch?v=iszwuX1AK6A",
                             "Martin Scorsese")

the_prestige = movie_class.Movie("The Prestige",
                             "A gripping tale of the relentless competition and inevitable escalation between two rival magicians.",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/the-prestige-2007/large_5MXyQfz8xUP3dIFPTubhTsbFY6N.jpg",
                             "https://www.youtube.com/watch?v=o4gHCmTQDVI",
                             "Christopher Nolan")

shutter_island = movie_class.Movie("Shutter Island",
                             "An investigator travels to a remote hospital for the criminally insane to investigate the disappearance of a convict.",
                             "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                             "Martin Scorsese")

# Create a list consisting of the above Movie instances.

movies = [gladiator, inception, momento, the_dark_knight_rises, interstellar, guardians_of_the_galaxy, the_wolf_of_wall_street, the_prestige, shutter_island]

# Run open_movies_page using our list of Movie instances defined.

movie_spot.open_movies_page(movies)
