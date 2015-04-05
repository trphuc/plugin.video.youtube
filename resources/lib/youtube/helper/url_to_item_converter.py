import re

__author__ = 'bromix'

import urlparse
from resources.lib.kodion.items import VideoItem, DirectoryItem
from . import utils


class UrlToItemConverter(object):
    def __init__(self):
        self._video_id_dict = {}
        self._video_items = []

        self._playlist_id_dict = {}
        self._playlist_items = []

        self._channel_id_dict = {}
        self._channel_items = []
        pass

    def add_url(self, url, provider, context):
        url_components = urlparse.urlparse(url)
        if url_components.hostname.lower() == 'youtube.com' or url_components.hostname.lower() == 'www.youtube.com':
            params = dict(urlparse.parse_qsl(url_components.query))
            if url_components.path.lower() == '/watch':
                video_id = params.get('v', '')
                if video_id:
                    plugin_uri = context.create_uri(['play'], {'video_id': video_id})
                    video_item = VideoItem('', plugin_uri)
                    self._video_id_dict[video_id] = video_item
                    pass

                playlist_id = params.get('list', '')
                if playlist_id:
                    playlist_item = DirectoryItem('', context.create_uri(['playlist', playlist_id]))
                    playlist_item.set_fanart(provider.get_fanart(context))
                    self._playlist_id_dict[playlist_id] = playlist_item
                    pass
                pass
            elif url_components.path.lower() == '/playlist':
                playlist_id = params.get('list', '')
                if playlist_id:
                    playlist_item = DirectoryItem('', context.create_uri(['playlist', playlist_id]))
                    playlist_item.set_fanart(provider.get_fanart(context))
                    self._playlist_id_dict[playlist_id] = playlist_item
                    pass
                pass
            else:
                context.log_debug('Unknown path "%s"' % url_components.path)
                pass
            pass
        pass

    def add_urls(self, urls, provider, context):
        for url in urls:
            self.add_url(url, provider, context)
            pass
        pass

    def get_video_items(self, provider, context):
        if len(self._video_items) == 0:
            channel_id_dict = {}
            utils.update_video_infos(provider, context, self._video_id_dict, None, channel_id_dict)
            utils.update_channel_infos(provider, context, channel_id_dict)

            for key in self._video_id_dict:
                video_item = self._video_id_dict[key]
                if video_item.get_title():
                    self._video_items.append(video_item)
                    pass
                pass
            pass

        return self._video_items

    def get_playlist_items(self, provider, context):
        if len(self._playlist_items) == 0:
            channel_id_dict = {}
            utils.update_playlist_infos(provider, context, self._playlist_id_dict, channel_id_dict)
            utils.update_channel_infos(provider, context, channel_id_dict)

            for key in self._playlist_id_dict:
                playlist_item = self._playlist_id_dict[key]
                if playlist_item.get_name():
                    self._playlist_items.append(playlist_item)
                    pass
                pass
            pass

        return self._playlist_items

    def get_channel_items(self, provider, context):
        if len(self._channel_items) == 0:
            channel_id_dict = {}
            utils.update_channel_infos(provider, context, channel_id_dict)

            for key in self._channel_id_dict:
                channel_item = self._channel_id_dict[key]
                if channel_item.get_name():
                    self._channel_items.append(channel_item)
                    pass
                pass
            pass

        return self._channel_items

    pass
