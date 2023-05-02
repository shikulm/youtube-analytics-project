from src.video import *
import pytest

@pytest.fixture()
def video1():
    return Video('9lO06Zxhu88')


def test_video__init__():
    video1 = Video('9lO06Zxhu88')
    assert video1.video_id == "9lO06Zxhu88"
    assert video1.video_title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video1.video_url == "https://youtu.be/9lO06Zxhu88"
    assert video1.video_count >= 0
    assert video1.video_like_count >= 0


def test_video__str__(video1):
    assert str(video1) == video1.video_title
