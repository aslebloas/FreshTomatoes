import fresh_tomatoes
import media


# Movies Instances

toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter",
                        "A Story of a boy an his toys that come to life")

avatar = media.Movie("Avatar",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                      "James Cameron",
                      "A marine on an alien planet")

dances_with_wolves = media.Movie("Dances with wolves",
                                "http://t1.gstatic.com/images?q=tbn:ANd9GcRxXOfHVrSwFqotyrBhQw6LwksRdtdKNncRRBjh8bU_yAyl7f3F",
                                "https://www.youtube.com/watch?v=HOlnsHFO84I",
                                "Kevin Costner",
                                "A Civil War soldier develops a relationship with a band of Lakota Indians.")


the_wolf_of_wallstreet = media.Movie("Dances with wolves",
                                "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                "https://www.youtube.com/watch?v=iszwuX1AK6A",
                                "Martin Scorsese",
                                "In 1987, Jordan Belfort (Leonardo DiCaprio) takes an entry-level job at a Wall Street brokerage firm.")

back_to_the_future_2 = media.Movie("Back to the Future Part II",
                                "https://upload.wikimedia.org/wikipedia/en/c/c2/Back_to_the_Future_Part_II.jpg",
                                "https://www.youtube.com/watch?v=rRrSp6Pqlz4",
                                "Robert Zemeckis",
                                "In this zany sequel, time-traveling duo Marty McFly (Michael J. Fox) and Dr. Emmett Brown (Christopher Lloyd) return from saving Marty's future son from disaster, only to discover their own time transformed.")

american_history_x = media.Movie("American History X",
                                "http://www.movieposter.com/posters/archive/main/92/MPW-46054",
                                "https://www.youtube.com/watch?v=JsPW6Fj3BUI",
                                "Tony Kaye",
                                "Living a life marked by violence and racism, neo-Nazi Derek Vinyard (Edward Norton) finally goes to prison after killing two black youths who tried to steal his car.")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                                "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                                "www.youtube.com/watch?v=yE-f1alkq9I",
                                "Michel Gondry",
                                "After a painful breakup, Clementine (Kate Winslet) undergoes a procedure to erase memories of her former boyfriend Joel (Jim Carrey) from her mind.")



# MusicVideos Instances

billie_jean = media.MusicVideo("Billie Jean",
                                "https://upload.wikimedia.org/wikipedia/en/2/2b/Billie_Jean_music_video.jpg",
                                "www.youtube.com/watch?v=Zi_XLOBDo_Y",
                                "Steve Barron",
                                "Michael Jackson")

total_eclipse = media.MusicVideo("Total Eclipse Of The Heart",
                                    "https://upload.wikimedia.org/wikipedia/en/0/09/Total_Eclipse_of_the_Heart_-_single_cover.jpg",
                                    "www.youtube.com/watch?v=lcOxhH8N3Bo",
                                    "Russell Mulcahy",
                                    "Bonnie Tyler")

bohemian_rhapsody = media.MusicVideo("Bohemian Rhapsody", 
                                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Bohemian_Rhapsody.png", 
                                        "www.youtube.com/watch?v=vsl3gBVO2k4", 
                                        "Bruce Gowers",
                                        "Queen")

da_funk = media.MusicVideo("Da Funk", 
                            "https://upload.wikimedia.org/wikipedia/en/2/24/Dafunk.jpg", 
                            "www.youtube.com/watch?v=mmi60Bd4jSs", 
                            "Spike Jonze",
                            "Daft Punk")



come_to_daddy = media.MusicVideo("Come To Daddy", 
                                    "https://upload.wikimedia.org/wikipedia/en/c/c9/Aphex_Twin_-_Come_to_Daddy.png", 
                                    "www.youtube.com/watch?v=h-9UvrLyj3k", 
                                    "Chris Cunningham",
                                    "Aphex Twin")

# List of Movies
movies = [toy_story, avatar, dances_with_wolves, the_wolf_of_wallstreet, back_to_the_future_2, american_history_x, eternal_sunshine]

# List of Music Videos
music_videos = [billie_jean, total_eclipse, bohemian_rhapsody, da_funk, come_to_daddy]

# Method to launch page
fresh_tomatoes.open_movies_page(movies)
