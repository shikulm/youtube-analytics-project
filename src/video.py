from src.channel import Channel
import json

class Video:
    youtube = Channel.get_service()

    def __init__(self, video_id):
        self.__video_id = video_id
        self.__video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title: str = self.__video_response['items'][0]['snippet']['title']
        self.video_url: str = f"https://youtu.be/{self.__video_id}"
        self.video_count: int = int(self.__video_response['items'][0]['statistics']['viewCount'])
        self.video_like_count: int = int(self.__video_response['items'][0]['statistics']['likeCount'])


    def __str__(self):
        return self.video_title

    @property
    def video_id(self):
        return self.__video_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__video_response, indent=2, ensure_ascii=False))


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


