from scrapy import Spider


class VideoSpider(Spider):

    name = 'video'
    start_urls = ['https://www.youtube.com/']

    custom_settings = {
        'VIDEOS_STORE': './',
        'ITEM_PIPELINES': {
            'origami.scrapy_pipelines.video.VideosPipeline': 100
        }
    }

    def parse(self, response, **kwargs):
        yield {
            'video_url': "https://www.youtube.com/watch?v=QJie7dTvbjQ",
            'meta': {
                'download_tool': 'youtube-dl', # value 'you-get' will use you-get
                'filename': 'QJie7dTvbjQ'
            }
        }
