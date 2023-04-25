from googleapiclient.discovery import build  # type: ignore
from config.config import YOUTUBE_ID


class YouTubeConnector:
    __service_object = None
    is_connected = False

    @classmethod
    def __init__(cls):
        if not cls.is_connected:
            cls.connect()

    @classmethod
    def connect(cls):
        """connect with youtube and create special connector object"""
        api_key: str = YOUTUBE_ID  # type: ignore
        # создать специальный объект для работы с API
        youtube_build = build('youtube', 'v3', developerKey=api_key)
        if youtube_build:
            cls.__service_object = youtube_build
            cls.is_connected = True

    @classmethod
    def get_service(cls):
        """ just return connectionn-object for other services"""
        if cls.__service_object:
            return cls.__service_object


if __name__ == '__main__':
    s = YouTubeConnector().get_service()
    print(s)
