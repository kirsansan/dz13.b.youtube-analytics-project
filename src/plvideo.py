from src.video import Video


class PLVideo(Video):

    def __init__(self, id_video, play_list_id=None):
        super().__init__(id_video)
        self.play_list_id = play_list_id