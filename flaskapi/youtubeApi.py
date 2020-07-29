import os
from googleapiclient.discovery import build


class YoutubeApi():

    api_key = os.environ.get('YOUTUBE_API_KEY')
    youtube_object = build('youtube', 'v3', developerKey=api_key)


    def getInfoVideos(self, id):

        infoVideos_list = []
        
        request = self.youtube_object.playlistItems().list(part='snippet', playlistId=id)
        videos = request.execute()

        # print(videos)

        info_videos = [video['snippet'] for video in videos['items']]

        for info in info_videos:
            video = {}

            video['id'] = info['position']
            video['urlThumbnail'] = info['thumbnails']['medium']['url']
            video['idVideo'] = info['resourceId']['videoId']
            video['name'] = info['title']

            infoVideos_list.append(video)

        return infoVideos_list



