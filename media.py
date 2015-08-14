import webbrowser


# Parent class
class Video():
    def __init__(self, title, image, video_url, director):
        self.title = title
        self.image = image
        self.video_url = video_url
        self.director = director

    def show_video(self):
        webbrowser.open(self.video_url)


# Child classes
class MusicVideo(Video):
    def __init__(self, title, image, video_url, director, artist):
        Video.__init__(self, title, image, video_url, director)
        self.artist = artist


class Movie(Video):

    def __init__(self, title, image, video_url, director, storyline):
        Video.__init__(self, title, image, video_url, director)
        self.storyline = storyline


class Serie(Video):

    def __init__(self, title, image, season, episode):
        Video.init__init__(self, title, image)
        self.season = season
        self.episode = episode
