一些个人 开发&整理 的小工具, 目前包含 (后续有需求再开发吧):

- scrapy_pipelines

若要使用, 先 `clone` 到本地, 然后:

``` shell
cd ./origami
python3 ./setup.py install
```
 
## Scrapy pipelines
 
### VideoPipelines

帮助快速开发一个简单的 [Scrapy](https://github.com/scrapy/scrapy) 视频爬虫, 使用 [Youtube-DL](https://github.com/ytdl-org/youtube-dl) OR [You-Get](https://github.com/soimort/you-get) 下载视频， 例子 `example/video.py`:

``` python
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
```

在该 py 文件同级目录执行:

```shell
scrapy runspider ./video.py
```

视频文件将会被存储在 `VIDEOS_STORE` 下, 且前缀为 `QJie7dTvbjQ`

> 使用 `youtube-dl` 时不推荐重命名, 会使得 `youtube-dl` 重复下载相同的文件
, `you-get` 随意
