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


if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    # vdud.print_info()

    print(type(Channel.get_service()))

    # получаем значения атрибутов
    # print(vdud.title)  # вДудь
    # print(vdud.video_count)  # 163 (может уже больше)
    # print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA


    # video_id = '4jRSy-_CLFg'  # Редакция плейлист анти-тревел
    # video_response = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
    #                                        id=video_id
    #                                        ).execute()
    # print(json.dumps(video_response, indent=2, ensure_ascii=False))
    #
    # # vdud.printj(video_response)
    # video_title: str = video_response['items'][0]['snippet']['title']
    # view_count: int = video_response['items'][0]['statistics']['viewCount']
    # like_count: int = video_response['items'][0]['statistics']['likeCount']
    # comment_count: int = video_response['items'][0]['statistics']['commentCount']