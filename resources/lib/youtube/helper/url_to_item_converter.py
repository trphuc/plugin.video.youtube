__author__ = 'bromix'


class UrlToItemConverter(object):
    def __init__(self):
        pass

    def add_url(self, url):
        url_components = urlparse.urlparse(url)
        if url_components.hostname.lower() == 'youtube.com' or url_components.hostname.lower() == 'www.youtube.com':
            if url_components.path.lower() == '/watch':
                params = dict(urlparse.parse_qsl(url_components.query))
                video_id = params.get('v', '')
                playlist_id = params.get('list', '')
                if playlist_id and video_id:
                    pass
                elif video_id:

                    pass
                elif playlist_id:
                    pass
                pass
            pass

        return None
        pass

    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)
            pass
        pass

    def get_items(self):
        return None

    pass
