import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics,contentDetails,topicDetails').execute()
        self.__title = self.channel['items'][0]['snippet']['title']
        self.__description = self.channel['items'][0]['snippet']['description']
        self.__url = "https://www.youtube.com/channel/" + self.channel_id
        # self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.__subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.__view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.__url})"

    def __add__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Неправильный тип данных аргумента')
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Неправильный тип данных аргумента')
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        """Проверка =="""
        if not isinstance(other, Channel):
            raise ValueError('Неправильный тип данных аргумента')
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        """Проверка !="""
        if not isinstance(other, Channel):
            raise ValueError('Неправильный тип данных аргумента')
        return self.subscriber_count != other.subscriber_count


    def __lt__(self, other):
        """Проверка <"""
        if not isinstance(other, Channel):
            raise ValueError('Неправильный тип данных аргумента')
        return self.subscriber_count < other.subscriber_count


    @classmethod
    def get_service(cls):
        """класс-метод get_service(), возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url


    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

    def to_json(self, file_name):
        """сохраняет в файл значения атрибутов экземпляра Channel"""
        #  Создаем словарь со значениями свойств
        dict_channel = {"channel_id": self.channel_id, "title": self.title, "description": self.description, "url": self.url, \
                        "subscriber_count": self.subscriber_count, "video_count": self.video_count, "view_count": self.view_count}

        # Сохрангяем в файл
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(dict_channel, f, indent=4, ensure_ascii=False)
