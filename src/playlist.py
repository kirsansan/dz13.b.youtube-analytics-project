import datetime
import json
from src.youtube_connector import YouTubeConnectorMixin
from src.video import Video
import isodate



class PlayList(YouTubeConnectorMixin):
    def __init__(self, id_playlist):
        self.__total_duration = None
        self.id_playlist = id_playlist
        self.__connector = self.get_connector()
        self.__content = self.get_info()
        self.__info = None
        self.__is_connected = False
        self.title = None
        self.url = None
        if self.__content:
            self.parse_info()
        else:
            pass


    def __repr__(self):
        return f"{self.__class__.__name__}({self.id_playlist}"

    def __str__(self):
        return f"{self.title}"

    def get_info(self):
        youtube = self.__connector
        playlist_videos = youtube.playlistItems().list(playlistId=self.id_playlist,
                                                       part='contentDetails, snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.__content = playlist_videos
        return playlist_videos

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.__content:
            print(self.__info)
        else:
            print("Not connected or parse error")


    def parse_info(self):
        """ set self.info as json and parse it"""
        if self.__content:
             self.__info = json.dumps(self.__content, indent=2, ensure_ascii=False)
             self.title = self.__content["items"][0]["snippet"]["title"]
             self.url = "https://www.youtube.com/playlist?list=" + self.id_playlist
        #     self.title_playlist = self.content["items"][0]["snippet"]["title"]
        #     self.url_video = self.content["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        #     tmp_likes_video: str = self.content["items"][0]["statistics"]["likeCount"]
        #     if tmp_likes_video.isdigit():
        #         self.likes_video = int(tmp_likes_video)
        #     tmp_video_count: str = self.content["items"][0]["statistics"]["viewCount"]
        #     if tmp_video_count.isdigit():
        #         self.view_count_video = int(tmp_video_count)
        pass

    @property
    def total_duration(self) -> datetime.timedelta:
        """
        calculate total duration for all videos in the  playlist
        :return: datetime.timedelta object
        """
        tmp_time_summary = datetime.timedelta(0)
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__content['items']]
        for vid_id in video_ids:
            video = Video(vid_id)
            iso_8601_duration = video.get_duration()
            duration = isodate.parse_duration(iso_8601_duration)
            tmp_time_summary += duration
            # print(type(tmp_time_summary))
        return tmp_time_summary




if __name__ == '__main__':
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # print(pl)
    # pl.print_info()
    #print(pl.total_duration())
    print("tdur=", pl.total_duration)
    print(type(pl.total_duration))
