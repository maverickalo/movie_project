# IMPORT ADDITIONAL FILES
import this
import media
import fresh_tomatoes

# CREATE MOVIE LIST BELOW

ten_questions = media.Movie(
              "10 Questions for the Dali Lama",
              "A man is granted 10 questions to ask the Dalai Lama. Which questions will he choose?",  # noqa
              "https://upload.wikimedia.org/wikipedia/en/0/0d/10_Questions_for_the_Dalai_Lama_%28movie_poster%29.jpg",  # noqa
              "https://www.youtube.com/watch?v=uPZmlqRQOO0")
interstellar = media.Movie(
              "Interstellar",
              "A little girls dad takes off into space in order to save the planet.",  # noqa
              "http://cdn1.sciencefiction.com/wp-content/uploads/2014/09/Interstellar.png",  # noqa
              "https://www.youtube.com/watch?v=0vxOhd4qlnA")
waking_life = media.Movie(
              "Waking Life",
              "Is he dreaming or is he awake?",
              "http://cdn.topdocumentaryfilms.com/wp-content/uploads/2011/08/waking-life-v2.jpg",   # noqa
              "https://www.youtube.com/watch?v=SbPgprcMtjo")
awake_the_life_of_yogananda = media.Movie(
              "Awake the Life of Yogananda",
              "The story of the Great Sage Yogananda",
              "http://xzusp5bnogtf69fh.zippykid.netdna-cdn.com/wp-content/uploads/2014/06/yogananda-poster-ss.jpg",   # noqa
              "https://www.youtube.com/watch?v=GyLkg3uDe1c")
samsara = media.Movie(
              "Samsara",
              "An amazing art film shot with an Ultra HD Camera",
              "https://upload.wikimedia.org/wikipedia/en/a/ad/Samsara_film.jpg",   # noqa
              "https://www.youtube.com/watch?v=qp967YAAdNk")
garden_state = media.Movie(
              "Garden State",
              "A young man discovers life when he starts coming off his medication",  # noqa
              "https://images-na.ssl-images-amazon.com/images/M/MV5BMjc5MDE0NjkxOF5BMl5BanBnXkFtZTcwNzA0NTkyMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",   # noqa
              "https://www.youtube.com/watch?v=u82n0e1mgmQ")
the_matrix = media.Movie(
              "The Matrix",
              "A man is awoken from a dreamstate to a Sci-Fi World",
              "https://images-na.ssl-images-amazon.com/images/I/51EG732BV3L.jpg",   # noqa
              "https://www.youtube.com/watch?v=vKQi3bBA1y8")
john_wick = media.Movie(
              "John Wick",
              "The russian mafia kills a mans dog. Turns out that man was John wick and he is not too happy about it.",   # noqa
              "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",   # noqa
              "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
contact = media.Movie(
              "Contact",
              "Jodi Foster discovers a sign from another world. Turns out its plans for a device to transport humans to space.",   # noqa
              "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",  # noqa
              "https://www.youtube.com/watch?v=SRoj3jK37Vc")
trainspotting = media.Movie(
              "Trainspotting",
              "The life of heroin and coming off it. ",
              "http://www.osmweasel.com/px/widgets/archive/imageupload/trainspotting-poster-1874220897.jpg",  # noqa
              "https://www.youtube.com/watch?v=8LuxOYIpu-I")
rock_n_rolla = media.Movie(
              "Rock n Rolla",
              "Several stories of theives intertwine in a strange way...",
              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0NTk5Mzk2OV5BMl5BanBnXkFtZTcwMDE3NTE4MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
              "https://www.youtube.com/watch?v=U0wQXw-UtSE")
the_royal_tenenbaums = media.Movie(
              "The Royal Tenenbaums",
              "The Story of a family that is extremely strange",
              "https://images-na.ssl-images-amazon.com/images/I/51rBK15mRTL.jpg",  # noqa
              "https://www.youtube.com/watch?v=8Eg6yIwP2vs")
gardians_of_the_galaxy = media.Movie(
              "Gardians of the Galaxy",
              "How will 5 friends come together to defend the galaxy?",
              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
              "https://www.youtube.com/watch?v=B16Bo47KS2g")

# CREATE THE ARRAY OF THE CREATED OBJECTS AND RUN THE FILE THROUGH FRESH_TOMATOES  # noqa

movies = [ten_questions, interstellar, waking_life,
          awake_the_life_of_yogananda, samsara, garden_state,
          the_matrix, john_wick, contact, trainspotting,
          rock_n_rolla, the_royal_tenenbaums,
          gardians_of_the_galaxy]

fresh_tomatoes.open_movies_page(movies)
