from src.video import PLVideo


class PlayList:

    # Полчаем ссылку на API youtube
    youtube = PLVideo.youtube
    def __init__(self, playlist_id):
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
        # print(playlists)

        # printj(playlists)
        # for playlist in playlists['items']:
        #     print(playlist)
        #     print()

        # playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
        #                                                part='snippet,contentDetails',
        #                                                maxResults=50,
        #                                                ).execute()
        # print(playlist_videos)
        # for playlist in playlist_videos['items']:
        #     print(playlist)
        #     print()


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')