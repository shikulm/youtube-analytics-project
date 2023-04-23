from src.channel import *
import pytest

@pytest.fixture()
def vdud():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

def test_init(vdud):
    # vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # получаем значения атрибутов
    assert vdud.title == "вДудь"
    assert vdud.video_count >= 163
    assert vdud.subscriber_count >= 10300000
    assert vdud.view_count >= 1984208634
    assert vdud.url == "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
    assert vdud.description == "Здесь задают вопросы"


def test_property_without_setter(vdud):
    with pytest.raises(AttributeError):
        vdud.channel_id = 'Новое название'









