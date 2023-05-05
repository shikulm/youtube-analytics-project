from src.video import PLVideo
import datetime

class PlayList:

    # Полчаем ссылку на API youtube
    youtube = PLVideo.youtube

    def __init__(self, playlist_id: str) -> None:
        """
        Инициализация свойств плэйлиста по его id
        """
        self.playlist_id = playlist_id

        # Извлекаем данные по Playlist

        self.playlists = self.youtube.playlists().list(id=self.playlist_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        self.title = self.playlists["items"][0]['snippet']["title"]
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"


        # Создание списка из видео плэфйлиста
        playlist_videos_dic = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='snippet,contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.playlist_videos = []

        # print(playlist_videos)
        for playlist in playlist_videos_dic['items']:
           self.playlist_videos.append(PLVideo(playlist['contentDetails']['videoId'], self.playlist_id))

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        return sum([el.duration for el in self.playlist_videos], datetime.timedelta())

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        max_video_like_count = max([el.video_like_count for el in self.playlist_videos])
        return [el.video_url for el in self.playlist_videos if el.video_like_count == max_video_like_count][0]




