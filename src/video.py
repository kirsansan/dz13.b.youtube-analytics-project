from src.channel import Channel
import json
from src.youtube_connector import YouTubeConnectorMixin
from src.channel import Channel



class Video(YouTubeConnectorMixin):

    def __init__(self, id_video):
        self.id_video = id_video
        self.__connector = self.get_connector()
        self.info = None              # will be filled by the update_info()
        self.content = None           # will be filled by the get_info()
        if self.__connector:
            self.is_connected = True
            self.get_info()
            self.parse_info()
        else:
            self.is_connected = False
            self.title_video = None
            self.url_video = None
            self.likes_video = None
            self.view_count_video = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_video}"

    def __str__(self):
        return f"{self.title_video}"


    def get_info(self):
        youtube = self.__connector
        request = youtube.videos().list(part="snippet,contentDetails,statistics", id=self.id_video)
        self.content = request.execute()

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.is_connected:
            print(self.info)

    def parse_info(self):
        """ set self.info as json and parse it"""
        if self.is_connected and self.content:
            self.info = json.dumps(self.content, indent=2, ensure_ascii=False)
            self.title_video = self.content["items"][0]["snippet"]["title"]
            self.url_video = "https://youtu.be/" + self.id_video
            tmp_likes_video: str = self.content["items"][0]["statistics"]["likeCount"]
            if tmp_likes_video.isdigit():
                self.likes_video = int(tmp_likes_video)
            tmp_video_count: str = self.content["items"][0]["statistics"]["viewCount"]
            if tmp_video_count.isdigit():
                self.view_count_video = int(tmp_video_count)


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
