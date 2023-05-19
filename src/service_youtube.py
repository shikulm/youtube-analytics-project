# необходимо установить через: pip install google-api-python-client
import os
from googleapiclient.discovery import build


class ServiceYoutube:
    """
    Класс-миксен для получения ссылки на API нщгегиу
    """

    def __init__(self):
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')
        # создать специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=api_key)
