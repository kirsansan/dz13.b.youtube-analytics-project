from src.video import Video

if __name__ == '__main__':
    broken_video = Video('XXXbroken_video_id14')
    print(broken_video.content)
    assert broken_video.title is None
    assert broken_video.like_count is None
