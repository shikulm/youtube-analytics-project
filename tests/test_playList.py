import pytest
from src.playlist import PlayList
from src.video import PLVideo
import datetime

@pytest.fixture()
def pl():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test__init__(pl):
    assert pl.title == "Редакция. АнтиТревел"
    assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"


def test_playlist_videos(pl):
    assert len(pl.playlist_videos) > 0
    assert isinstance(pl.playlist_videos, list)
    assert isinstance(pl.playlist_videos[0], PLVideo)


def test_total_duration(pl):
    """Тестирование метода total_duration"""
    duration = pl.total_duration
    assert str(duration) == "3:41:01"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 13261.0

def test_show_best_video(pl):
    assert pl.show_best_video() == "https://youtu.be/9Bv2zltQKQA"




