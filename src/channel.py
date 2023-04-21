from googleapiclient.discovery import build
from config.config import YOUTUBE_ID
import json


class Channel:
    all: list = []

    def __init__(self, channel_id="default"):
        self.channel_id = channel_id
        self.is_connected = False
        self.channel_name = None
        self.content = None
        self.info = None

    def connect(self):
        """connect with channel and fill self.content"""
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = YOUTUBE_ID  # type: ignore
        # создать специальный объект для работы с API
        youtube_build = build('youtube', 'v3', developerKey=api_key)
        if youtube_build:
            self.is_connected = True
            self.content = youtube_build.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.is_connected:
            self.set_info()
            print(self.info)


    def set_info(self):
        """ set self.info """
        if self.is_connected:
            self.info = json.dumps(self.content, indent=2, ensure_ascii=False)

    def get_title(self):
        """ parse title from content and print it """
        if self.is_connected:
            print(self.content["items"][0]["snippet"]["title"])






