import pytest
from src.playList import PlayList

@pytest.fixture()
def pl():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test__init__(pl):
    assert pl.title == "Редакция. АнтиТревел"
    assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"

