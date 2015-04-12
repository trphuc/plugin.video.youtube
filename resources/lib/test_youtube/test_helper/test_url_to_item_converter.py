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
        description = "Even lovable animated superhero movies have sins. And believe it or not, this is one of the most requested movies we haven't done yet. So here we are to rain on Big Hero 6. Jeremy wrote a book: http://theablesbook.com Thursday, Romance sins. Remember, no movie is without sin. Which movie's sins do YOU want to see recounted? Tweet us: http://twitter.com/cinemasins Tumble us: http://cinema-sins.tumblr.com Call us: 405-459-7466 Reddit with us: http://reddit.com/r/cinemasins"
        urls = extract_urls(description)
        context = kodion.Context()
        resolver = UrlResolver(context)
        res_urls = []
        for url in urls:
            res_urls.append(resolver.resolve(url))
            pass
        pass

        provider = Provider()
        context.set_localization(30502, 'Go to %s')
        url_converter = UrlToItemConverter(flatten=True)
        url_converter.add_urls(res_urls, provider, context)
        items = url_converter.get_items(provider, context)
        pass

    pass
