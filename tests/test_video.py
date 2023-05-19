from src.video import *
import pytest

@pytest.fixture()
def video1():
    return Video('9lO06Zxhu88')


@pytest.fixture()
def plvideo1():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


def test_video__init__():
    video1 = Video('9lO06Zxhu88')
    assert video1.video_id == "9lO06Zxhu88"
    assert video1.video_title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video1.video_url == "https://youtu.be/9lO06Zxhu88"
    assert video1.video_count >= 0
    assert video1.video_like_count >= 0

def test_video_error_id():
    with pytest.raises(ValueError):
        broken_video = Video('broken_video_id')
        assert broken_video.title is None
        assert broken_video.like_count is None


def test_video__str__(video1):
    assert str(video1) == video1.video_title

def test_plvideo__init__():
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert video2.video_id == 'BBotskuyw_M'
    assert video2.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'


def test_plvideo__str__(plvideo1):
    assert str(plvideo1) == 'Пушкин: наше все?'

