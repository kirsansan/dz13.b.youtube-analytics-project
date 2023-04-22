from googleapiclient.discovery import build
from config.config import YOUTUBE_ID, FILE_FOR_WRITE
import json


class Channel:
    all: list = []
    __service_name = None

    def __init__(self, channel_id="default"):
        self.__channel_id = channel_id
        self.is_connected = False
        self.channel_name = None
        self.content = None
        self.info = None
        self.title = None
        self.description = None
        self.url = None
        self.followers = None
        self.video_count = None
        self.view_count = None


    def connect(self):
        """connect with channel and fill self.content"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = YOUTUBE_ID  # type: ignore
        # создать специальный объект для работы с API
        youtube_build = build('youtube', 'v3', developerKey=api_key)
        if youtube_build:
            Channel.__service_name = youtube_build
            self.is_connected = True
            self.content = youtube_build.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    @classmethod
    def get_service(cls):
        """ just return content object for other services"""
        if cls.__service_name:
            return cls.__service_name


    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.is_connected:
            self.set_info()
            print(self.info)


    def set_info(self):
        """ set self.info """
        if self.is_connected:
            self.info = json.dumps(self.content, indent=2, ensure_ascii=False)

    def set_parameters(self):
        """ parse parameters from content and set it """
        if self.is_connected:
            self.title = self.content["items"][0]["snippet"]["title"]
            self.description = self.content["items"][0]["snippet"]["description"]
            self.url = self.content["items"][0]["snippet"]["thumbnails"]["default"]["url"]
            self.followers = self.content["items"][0]["statistics"]["subscriberCount"]
            self.video_count = self.content["items"][0]["statistics"]["videoCount"]
            self.view_count = self.content["items"][0]["statistics"]["viewCount"]


    def get_title(self):
        """ parse title from content and print it """
        if self.is_connected:
            print(self.content["items"][0]["snippet"]["title"])


    def to_json(self, filename=FILE_FOR_WRITE):
        """ save information to the file json format"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                    "title": self.title,
                    "description": self.description,
                    "url": self.url,
                    "video_count": self.video_count,
                    "viewCount": self.view_count
                    }, f, indent=2, ensure_ascii=False, separators=(',', ': '))

    @property
    def channel_id(self):
        return self.__channel_id
