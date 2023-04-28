import datetime
import json
from src.youtube_connector import YouTubeConnectorMixin
from src.video import Video
import isodate


class PlayList(YouTubeConnectorMixin):
    def __init__(self, id_playlist):
        self.__total_duration = None
        self.id_playlist = id_playlist
        self.title = None
        self.url = None
        self.__info = None
        self.__connector = self.get_connector()
        self.__content_info = self.get_info()
        self.__content_items = self.get_items()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.id_playlist}')"

    def __str__(self):
        return f"{self.title}"

    def get_items(self):
        youtube = self.__connector
        playlist_videos = youtube.playlistItems().list(playlistId=self.id_playlist,
                                                       part='contentDetails, snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.__content_items = playlist_videos
        return playlist_videos

    def get_info(self):
        youtube = self.__connector
        playlist_info = youtube.playlists().list(id=self.id_playlist,
                                                 part='snippet'
                                                 ).execute()
        self.__content_info = playlist_info
        self.__info = json.dumps(self.__content_info, indent=2, ensure_ascii=False)
        self.title = self.__content_info["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list=" + self.id_playlist
        return playlist_info

    def print_info(self):
        """ just touch set_info and print self.info"""
        if self.__content_info:
            print(self.__info)
        if self.__content_items:
            print(self.__content_items)
        if not self.__content_info and not self.__content_items:
            print("Not connected or parse error")

    @property
    def total_duration(self) -> datetime.timedelta:
        """
        calculate total duration for all videos in the  playlist
        :return: datetime.timedelta object
        """
        tmp_time_summary = datetime.timedelta(seconds=0)
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__content_items['items']]
        for vid_id in video_ids:
            video = Video(vid_id)
            iso_8601_duration = video.get_duration()
            duration = isodate.parse_duration(iso_8601_duration)
            tmp_time_summary += duration
        return tmp_time_summary

    def show_best_video(self):
        """ find the best video in playlist (video with maximum numver of views)
        :return: url video"""
        max_video_time = 0
        video_link = None
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__content_items['items']]
        for vid_id in video_ids:
            video = Video(vid_id)
            if video.count_views > max_video_time:
                video_link = video.url_video
                max_video_time = video.count_views
        return video_link


if __name__ == '__main__':
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # print(pl)
    # pl.print_info()
    print(pl.total_duration)
    print("tdur=", pl.total_duration)
    print(type(pl.total_duration))
    print(pl.show_best_video())
