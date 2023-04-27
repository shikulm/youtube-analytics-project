import googleapiclient.discovery
import json

from src.channel import *
import pytest

@pytest.fixture()
def vdud():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture()
def redactsiya():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')

def test__init__(vdud):
    # vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # получаем значения атрибутов
    assert vdud.title == "вДудь"
    assert vdud.video_count >= 163
    assert vdud.subscriber_count >= 10300000
    assert vdud.view_count >= 1984208634
    assert vdud.url == "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
    assert vdud.description == "Здесь задают вопросы"

def test__str__(vdud):
    assert str(vdud) == "вДудь (https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA)"


def test__add__(vdud, redactsiya):
    assert vdud + redactsiya == vdud.subscriber_count + redactsiya.subscriber_count

def test__add__ValueError(vdud):
    with pytest.raises(ValueError):
        vdud + 5


def test__sub__(vdud, redactsiya):
    assert vdud - redactsiya == vdud.subscriber_count - redactsiya.subscriber_count
    assert redactsiya - vdud == redactsiya.subscriber_count - vdud.subscriber_count

def test__sub__ValueError(vdud):
    with pytest.raises(ValueError):
        vdud - 5


def test__eq__(vdud, redactsiya):
    assert (vdud == redactsiya) == (vdud.subscriber_count == redactsiya.subscriber_count)


def test__eq__ValueError(vdud):
    with pytest.raises(ValueError):
        vdud == 5


def test__ne__(vdud, redactsiya):
    assert (vdud != redactsiya) == (vdud.subscriber_count != redactsiya.subscriber_count)


def test__ne__ValueError(vdud):
    with pytest.raises(ValueError):
        vdud != 5


def test__lt__(vdud, redactsiya):
    """Тест <"""
    assert (vdud < redactsiya) == (vdud.subscriber_count < redactsiya.subscriber_count)


def test__lt__ValueError(vdud):
    with pytest.raises(ValueError):
        vdud < 5


def test_property_without_setter(vdud):
    with pytest.raises(AttributeError):
        vdud.channel_id = 'Новое название'
        vdud.title = "Новый"
        vdud.video_count = 200
        vdud.subscriber_count = 256
        vdud.view_count = 345
        vdud.url = "новый url"
        vdud.description == "новое описание"


def test_get_service():
    API_YT = Channel.get_service()
    assert isinstance(API_YT, googleapiclient.discovery.Resource)


def test_json(vdud):
    vdud.to_json("vdud.json")

    with open("vdud.json", "r", encoding="utf-8") as f:
        dict_json = json.load(f)

    assert dict_json["channel_id"] == vdud.channel_id
    assert dict_json["title"] == vdud.title
    assert dict_json["description"] == vdud.description
    assert dict_json["url"] == vdud.url
    assert dict_json["subscriber_count"] == vdud.subscriber_count
    assert dict_json["video_count"] == vdud.video_count
    assert dict_json["view_count"] == vdud.view_count






