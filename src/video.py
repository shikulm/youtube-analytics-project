from channel import Channel
import json

class Video:
    youtube = Channel.get_service()

    def __init__(self, video_id):
        self.__video_id = video_id
        self.__video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.view_title = self.__video_response['items'][0]['snippet']['title']
        self.view_url = f"https://youtu.be/{self.__video_id}"
        self.view_count: int = self.__video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.__video_response['items'][0]['statistics']['likeCount']

    @property
    def video_id(self):
        return self.__video_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__video_response, indent=2, ensure_ascii=False))


video1 = Video('9lO06Zxhu88')
video1.print_info()