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
        description = 'Subscribe for more Nerdist News: http://nerdi.st/subscribe Watch the last episode: http://nerdi.st/1NHOv6e Find out how you can watch AVENGERS: AGE OF ULTRON early, plus comedy magician Justin Willman performs some Oreo cookie magic on Nerdist News with Jessica Chobot. More Marvel: http://nerdist.com/tag/marvel/ Watch more Nerdist News: http://bit.ly/1qvVVhV Follow Justin on the web: http://www.justinwillman.com/ https://twitter.com/justin_willman Follow Us: Nerdist News https://twitter.com/NerdistNews Nerdist.com https://twitter.com/NerdistDotCom Jessica Chobot https://twitter.com/JessicaChobot Dan Casey https://twitter.com/osteoferocious Malik Forté https://twitter.com/Malik4Play Kyle Hill https://twitter.com/sci_phile Nerdist News 5 days a week, Monday through Friday at 8am PST.'
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
