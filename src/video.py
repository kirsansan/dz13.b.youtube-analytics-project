from src.channel import Channel
import json
from src.youtube_connector import YouTubeConnector


class Video():

    def __init__(self, id_video):
        self.id_video = id_video
        self.__connector = YouTubeConnector().get_service()
        if self.__connector:
            self.is_connected = True
            self.get_info()
            self.apdate_info()
        else:
            self.is_connected = False
            self.title_video = None
            self.url_video = None
            self.likes_video = None
            self.content = None

    def get_info(self):
        youtube = self.__connector
        request = youtube.videos().list(part="snippet,contentDetails,statistics", id=self.id_video)
        self.content = request.execute()

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.is_connected:
            self.get_info()
            print(self.info)

    def apdate_info(self):
        """ set self.info """
        if self.is_connected:
            self.info = json.dumps(self.content, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    v = Video('9lO06Zxhu88')
    v.print_info()
