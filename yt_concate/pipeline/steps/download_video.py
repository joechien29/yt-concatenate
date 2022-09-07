from pytube import YouTube

from .step import Step
from yt_concate.settings import VIEDOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            else:
                print('downloading', url)
                YouTube(url).streams.get_highest_resolution().download(output_path=VIEDOS_DIR, filename=yt.id + '.mp4', skip_existing=True)

        return data
