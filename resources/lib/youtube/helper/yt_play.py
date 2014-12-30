__author__ = 'bromix'

from resources.lib import kodion
from resources.lib.kodion.items import VideoItem
from resources.lib.youtube.youtube_exceptions import YouTubeException
from resources.lib.youtube.helper import utils, v3


def play_video(provider, context, re_match):
    def _compare(item):
        vq = context.get_settings().get_video_quality()
        return vq - item['format']['height']

    try:
        video_id = context.get_param('video_id')
        client = provider.get_client(context)
        video_streams = client.get_video_streams(context, video_id)
        video_stream = kodion.utils.find_best_fit(video_streams, _compare)

        video_item = VideoItem(video_id, video_stream['url'])
        video_id_dict = {video_id: video_item}
        utils.update_video_infos(provider, context, video_id_dict)

        # Auto-Remove video from 'Watch Later' playlist - this should run asynchronous
        if provider.is_logged_in() and context.get_settings().get_bool('youtube.playlist.watchlater.autoremove',
                                                                       True):
            command = 'RunPlugin(%s)' % context.create_uri(['internal', 'auto_remove_watch_later'],
                                                           {'video_id': video_id})
            context.execute(command)
            pass

        return video_item
    except YouTubeException, ex:
        message = ex.get_message()
        message = kodion.utils.strip_html_from_text(message)
        context.get_ui().show_notification(message, time_milliseconds=30000)
        pass

    pass


def play_playlist(provider, context, re_match):
    playlist_id = context.get_param('playlist_id')
    order = context.get_param('order', 'default')
    client = provider.get_client(context)

    videos = []

    def _load_videos(_page_token=''):
        json_data = client.get_playlist_items(playlist_id, page_token=_page_token)
        next_page_token = json_data.get('nextPageToken', '')
        if next_page_token:
            del json_data['nextPageToken']
            pass

        if not v3.handle_error(provider, context, json_data):
            return False
        videos.extend(v3.response_to_items(provider, context, json_data))

        if next_page_token:
            _load_videos(next_page_token)
            pass
        pass

    _load_videos()
    if order == 'reverse':
        videos = videos[::-1]
        pass
    for video in videos:
        print video
        pass
    pass