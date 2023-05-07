import json
from src.youtube_connector import YouTubeConnectorMixin
from src.errors_class import MyHttpError
from googleapiclient.errors import HttpError  # useless import
import requests  # for a test


class Video(YouTubeConnectorMixin):

    def __init__(self, id_video):
        self.id_video = id_video
        self.__connector = self.get_connector()
        self.content = None  # will be filled by the get_info()
        self.info = None  # will be filled by the parse_info()
        self.is_connected = False
        self.title = None
        self.url_video = None
        self.like_count = None
        self.view_count_video = None
        if self.__connector:
            self.is_connected = True
            self.get_info()
            self.parse_info()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_video}"

    def __str__(self):
        return f"{self.title}"

    def get_info(self):
        youtube = self.__connector
        try:
            request = youtube.videos().list(part="snippet,contentDetails,statistics", id=self.id_video)
            self.content = request.execute()
        except Exception as err:
            print("Chief, all is disappeared", err)

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.is_connected:
            print(self.info)

    def parse_info(self):
        """ set self.info as json and parse it"""
        if self.is_connected and self.content:
            try:
                if not self.content["items"]:
                    raise MyHttpError(404, "Video not found")
                self.info = json.dumps(self.content, indent=6, ensure_ascii=False)
                self.title = self.content["items"][0]["snippet"]["title"]
                self.url_video = "https://youtu.be/" + self.id_video
                tmp_like_count: str = self.content["items"][0]["statistics"]["likeCount"]
                if tmp_like_count.isdigit():
                    self.like_count = int(tmp_like_count)
                tmp_video_count: str = self.content["items"][0]["statistics"]["viewCount"]
                if tmp_video_count.isdigit():
                    self.view_count_video = int(tmp_video_count)
            except MyHttpError as e:
                print("Bad video reference ", {e})


    def get_duration(self) -> str:
        """Returns the duration of the video"""
        if self.content:
            duration = self.content["items"][0]["contentDetails"]["duration"]
            return duration

    @property
    def count_views(self) -> int:
        """return count of view the video"""
        return self.view_count_video


if __name__ == '__main__':
    v1 = Video('9lO06Zxhu88')
    # v.print_info()
    # print(v1)
    v2 = Video('BBotskuyw_M')
    v2.print_info()
    print(v2)
    print(v1.get_duration())
    # ch = Channel("UCNYejKoEJ84iGgXPwTBkCCg")
    # print(ch)
    ve = Video('bad_link_to_non_exist_video')


