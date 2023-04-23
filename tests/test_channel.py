from src.channel import *
import pytest


def test_init():
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # получаем значения атрибутов
    assert vdud.title == "вДудь"
    assert vdud.video_count >= 163
    assert vdud.subscriber_count >= 10300000
    assert vdud.view_count >= 1984208634
    assert vdud.url == "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
    assert vdud.description == "Здесь задают вопросы"








