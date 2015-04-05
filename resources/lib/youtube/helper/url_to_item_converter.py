import re

__author__ = 'bromix'

import urlparse
from resources.lib.kodion.items import VideoItem, DirectoryItem
from . import utils


class UrlToItemConverter(object):
    def __init__(self):
        self._video_id_dict = {}
        self._video_items = []
        self._video_items_updated = False

        self._playlist_id_dict = {}
        self._playlist_items = []
        self._playlist_items_updated = False

        self._channel_id_dict = {}
        self._channel_items = []
        self._channel_items_updated = False
        pass

    def add_url(self, url, provider, context):
        url_components = urlparse.urlparse(url)
        if url_components.hostname.lower() == 'youtube.com' or url_components.hostname.lower() == 'www.youtube.com':
            params = dict(urlparse.parse_qsl(url_components.query))
            if url_components.path.lower() == '/watch':
                video_id = params.get('v', '')
                playlist_id = params.get('list', '')
                if video_id:
                    plugin_uri = context.create_uri(['play'], {'video_id': video_id})
                    # we try to replicate the behavior of the original link a start the playlist with a given video
                    if playlist_id:
                        plugin_uri = context.create_uri(['play'], {'video_id': video_id, 'playlist_id': playlist_id})
                        pass
                    video_item = VideoItem('dummy', plugin_uri)
                    if provider is not None:
                        video_item.set_fanart(provider.get_fanart(context))
                        pass
                    self._video_id_dict[video_id] = video_item
                    self._video_items.append(video_item)
                    pass
                pass
            elif url_components.path.lower() == '/playlist':
                playlist_id = params.get('list', '')
                if playlist_id:
                    playlist_item = DirectoryItem('dummy', context.create_uri(['playlist', playlist_id]))
                    playlist_item.set_fanart(provider.get_fanart(context))
                    self._playlist_items.append(playlist_item)
                    self._playlist_id_dict[playlist_id] = playlist_item
                    pass
                pass
            else:
                context.log_debug('Unknown path "%s"' % url_components.path)
                pass
            pass

        return None
        pass

    def add_urls(self, urls, provider, context):
        for url in urls:
            self.add_url(url, provider, context)
            pass
        pass

    def get_video_items(self, provider, context):
        if not self._video_items_updated:
            channel_id_dict = {}
            utils.update_video_infos(provider, context, self._video_id_dict, None, channel_id_dict)
            utils.update_channel_infos(provider, context, channel_id_dict)
            self._video_items_updated = True
            pass

        return self._video_items

    def get_playlist_items(self, provider, context):
        if not self._playlist_items_updated:
            channel_id_dict = {}
            utils.update_playlist_infos(provider, context, self._playlist_id_dict, channel_id_dict)
            utils.update_channel_infos(provider, context, channel_id_dict)
            self._playlist_items_updated = True
            pass

        return self._playlist_items

    def get_channel_items(self, provider, context):
        if not self._channel_items_updated:
            channel_id_dict = {}
            utils.update_channel_infos(provider, context, channel_id_dict)
            self._channel_items_updated = True
            pass

        return self._channel_items

    pass
