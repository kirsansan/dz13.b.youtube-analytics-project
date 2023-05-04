from googleapiclient.discovery import build  # type: ignore
from config.config import YOUTUBE_ID


class YouTubeConnectorMixin:
    __connector = None

    @classmethod
    def get_connector(cls):
        """connect with youtube and create special connector object
        :return: special object
        """
        if cls.__connector == None:
            api_key: str = YOUTUBE_ID  # type: ignore
            # создать специальный объект для работы с API
            youtube_build = build('youtube', 'v3', developerKey=api_key)
            if youtube_build:
                cls.__connector = youtube_build
                return youtube_build
        else:
            return cls.__connector


if __name__ == '__main__':
    s1 = YouTubeConnectorMixin()
    s2 = YouTubeConnectorMixin()
    s3 = YouTubeConnectorMixin()
    print(s1.get_connector())
    print(s2.get_connector())
    print(s3.get_connector())
    p = YouTubeConnectorMixin().get_connector()
    print(p)
