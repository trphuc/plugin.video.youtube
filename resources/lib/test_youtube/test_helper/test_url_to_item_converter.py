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
        description = '(http://www.youtubAlle FSK16 und 18 Filme findest du auf http://www.netzkino.de und der gratis Netzkino App! Netzkino Android App - https://play.google.com/store/apps/details?id=de.netzkino.android.ics Netzkino iOS App - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 .................................................................. KIFFERWAHN Völlig abgedrehte Musical-Komödie mit Kristen Bell von 2005. Mit: Christian Campbell, Neve Campbell | Regie: Andy Fickman FSK: Freigegeben ab 12 Jahren .................................................................. NETZKINO ABONNIEREN: https://www.youtube.com/user/Netzkino?sub_confirmation=1 .................................................................. NETZKINO ANDROID APP herunterladen - https://play.google.com/store/apps/details?id=de.netzkino.android.ics NETZKINO iOS APP herunterladen - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 NETZKINO WINDOWS 8 APP herunterladen - http://apps.microsoft.com/windows/de-de/app/netzkino/fc8ac95f-b14e-44ef-a148-9a4c7bec7919 NETZKINO WINDOWS PHONE APP herunterladen - http://www.windowsphone.com/de-de/store/app/netzkino/3734d2e8-c646-472d-94cb-fc021505867c NETZKINO AMAZON APP herunterladen - http://www.amazon.de/Netzkino-Services-GmbH/dp/B00MR1YQM8 FACEBOOK - https://www.facebook.com/netzkino. TWITTER - https://twitter.com/netzkino GOOGLE+ - https://plus.google.com/+netzkino NETZKINO.DE - http://www.netzkino.de .................................................................. INHALTSANGABE: Jimmy und Mary, das amerikanische Vorzeige-Teenagerpaar schlechthin, bereiten sich auf eine Englisch-Prüfung an der High-School und ein erfülltes Familienleben vor. Doch Jimmy gerät in die Fänge des Marihuana-Dealers und Jazz-Freaks Jack. Ein Zug an der Haschischzigarette und der saubere Jimmy verwandelt sich in ein unmoralisches Monster, das nur noch auf Sex, Anarchie und dem nächsten Joint lechtzt. Widerwärtige Ausschweifungen, Tote, Irrsinn und schwerste Rechtsverletzungen sind die Folge des Stoffes, der Amerika zu vernichten droht. Jimmy und seine neuen Freunde stellen im Drogenrausch die furchtbarsten Dinge an, ständig begleitet von infernalischer Musik. Das schonungslose Ende naht, als die sonst so brave Mary im Rausch des Giftes ihre Qualitäten als Domina entdeckt. COPYRIGHT: Die Lizenz zur Veröffentlichung des Filmes auf Youtube wurde erworben von: Koch Media GmbH. .................................................................. LUST AUF MEHR FILME? Paradise Trouble: http://bit.ly/1m7iawz Neu bei Netzkino: http://bit.ly/PcVRYy HD-Kino: http://bit.ly/1hdR7Ym Actionfilme: http://bit.ly/1fJdA0b Komödien: http://bit.ly/1huGe96 Horrorfilme: http://bit.ly/1huGeWI Thriller: http://bit.ly/1gWMLL3 Alle Playlists: http://bit.ly/1hXRU0z ..................................................................'
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
