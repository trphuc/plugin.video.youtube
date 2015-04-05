#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__ = 'bromix'

from resources.lib import kodion
from resources.lib.youtube import Provider
from resources.lib.youtube.helper import UrlToItemConverter
from resources.lib.youtube.helper import UrlResolver
from resources.lib.youtube.helper import extract_urls
import unittest


class TestUrlExtract(unittest.TestCase):
    def test_complete_sequence(self):
        description = (
            'You can play the Forza Horizon 2 Presents Fast & Furious Standalone Pack FOR FREE until April 10! http://bit.ly/1GNrS0a\n'
            'Sponsored Content. Special consideration provided by XBOX.\n'
            '\n'
            'Joven, Ian, and Anthony traverse Southern France in the brand new Standalone Pack from Forza Horizon 2 featuring the cars and missions of the Fast & Furious films. Can you beat our times? Send us a screenshot!\n'
            '\n'
            'Subscribe to Smosh Games ►► http://smo.sh/SubscribeSmoshGames\n'
            'Jovenshire gets Lost in Italy ►► http://smo.sh/LostItaly\n'
            '\n'
            'Play with us!\n'
            'Subscribe: http://smo.sh/SubscribeSmoshGames\n'
            'Like us on Facebook: http://facebook.com/SmoshGames\n'
            'Follow us on Twitter: http://twitter.com/SmoshGames\n'
            'Add us to your circles on Google+: http://google.com/+SmoshGames'
        )
        urls = extract_urls(description)
        resolver = UrlResolver()
        res_urls = []
        for url in urls:
            res_urls.append(resolver.resolve(url))
            pass
        pass

        provider = Provider()
        context = kodion.Context()
        context.set_localization(30502, 'Go to %s')
        url_converter = UrlToItemConverter()
        url_converter.add_urls(res_urls, provider, context)
        items = url_converter.get_video_items(provider, context)
        items = url_converter.get_playlist_items(provider, context)
        pass

    pass
