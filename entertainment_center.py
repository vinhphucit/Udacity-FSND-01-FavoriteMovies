import media
import fresh_tomatoes

# declare movies 
seven = media.Movie("Seven",
                    "When retiring police Detective William Somerset (Morgan Freeman) tackles a final case with the aid of newly transferred David Mills (Brad Pitt), they discover a number of elaborate and grizzly murders. They soon realize they are dealing with a serial killer (Kevin Spacey) who is targeting people he thinks represent one of the seven deadly sins. Somerset also befriends Mills' wife, Tracy (Gwyneth Paltrow), who is pregnant and afraid to raise her child in the crime-riddled city.",
                    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE"
                    )

fightclub = media.Movie("Fight Club",
                        "A depressed man (Edward Norton) suffering from insomnia meets a strange soap salesman named Tyler Durden (Brad Pitt) and soon finds himself living in his squalid house after his perfect apartment is destroyed. The two bored men form an underground club with strict rules and fight other men who are fed up with their mundane lives. Their perfect partnership frays when Marla (Helena Bonham Carter), a fellow support group crasher, attracts Tyler's attention.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg"
                        )

thecuriouscaseofbenjaminbutton = media.Movie("The Curious Case of Benjamin Button",
                                             "Born under unusual circumstances, Benjamin Button (Brad Pitt) springs into being as an elderly man in a New Orleans nursing home and ages in reverse. Twelve years after his birth, he meets Daisy, a child who flickers in and out of his life as she grows up to be a dancer (Cate Blanchett). Though he has all sorts of unusual adventures over the course of his life, it is his relationship with Daisy, and the hope that they will come together at the right time, that drives Benjamin forward.",
                                             "https://upload.wikimedia.org/wikipedia/en/7/7c/The_Curious_Case_of_Benjamin_Button_%28film%29.png",
                                             "https://www.youtube.com/watch?v=VqeqaweXBV0"
                                             )
fury = media.Movie("Fury",
                   "In April 1945, the Allies are making their final push in the European theater. A battle-hardened Army sergeant named Don \"Wardaddy\" Collier (Brad Pitt), leading a Sherman tank and a five-man crew, undertakes a deadly mission behind enemy lines. Hopelessly outnumbered, outgunned and saddled with an inexperienced soldier (Logan Lerman) in their midst, Wardaddy and his men face overwhelming odds as they move to strike at the heart of Nazi Germany.",
                   "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg"
                   )

snatch = media.Movie("Snatch",
                     "Illegal boxing promoter Turkish (Jason Statham) convinces gangster Brick Top (Alan Ford) to offer bets on bare-knuckle boxer Mickey (Brad Pitt) at his bookie business. When Mickey does not throw his first fight as agreed, an infuriated Brick Top demands another match. Meanwhile, gangster Frankie Four Fingers (Benicio Del Toro) comes to place a bet for a friend with Brick Top's bookies, as multiple criminals converge on a stolen diamond that Frankie has come to London to sell.",
                     "http://www.imfdb.org/images/b/b1/Snatch_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

# add movies to an array
movies = [seven, fightclub, thecuriouscaseofbenjaminbutton, fury, snatch]

# generate website with above movies
fresh_tomatoes.open_movies_page(movies)
