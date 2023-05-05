import pytest
from src.playList import PlayList
from src.video import PLVideo

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


