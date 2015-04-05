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
        description = 'Alle FSK16 und 18 Filme findest du auf http://www.netzkino.de und der gratis Netzkino App! Netzkino Android App - https://play.google.com/store/apps/details?id=de.netzkino.android.ics Netzkino iOS App - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 .................................................................. SECOND CHANCE - ALLES WIRD GUT Die Mafia-Komödie mit Burt Reynolds (Boogie Nights) von 2000. Mit: Richard Dreyfuss, Dan Hedaya | Regie: Michael Dinner FSK: Freigegeben ab 12 Jahren .................................................................. NETZKINO ABONNIEREN: https://www.youtube.com/user/Netzkino?sub_confirmation=1 .................................................................. NETZKINO ANDROID APP herunterladen - https://play.google.com/store/apps/details?id=de.netzkino.android.ics NETZKINO iOS APP herunterladen - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 NETZKINO WINDOWS 8 APP herunterladen - http://apps.microsoft.com/windows/de-de/app/netzkino/fc8ac95f-b14e-44ef-a148-9a4c7bec7919 NETZKINO WINDOWS PHONE APP herunterladen - http://www.windowsphone.com/de-de/store/app/netzkino/3734d2e8-c646-472d-94cb-fc021505867c NETZKINO AMAZON APP herunterladen - http://www.amazon.de/Netzkino-Services-GmbH/dp/B00MR1YQM8 FACEBOOK - https://www.facebook.com/netzkino. TWITTER - https://twitter.com/netzkino GOOGLE+ - https://plus.google.com/+netzkino NETZKINO.DE - http://www.netzkino.de .................................................................. INHALTSANGABE: Sie sind alt. Sie sind in Rente. Aber sie haben nichts verlernt. Die Ex-Mafiosi Bobby, Joey, Mike und Tony haben sich im sonnigen South Beach, Miami, zur Ruhe gesetzt. Doch die vier Senioren müssen noch einmal in ihre Trickkiste greifen: Ihr Altersruhesitz, das heruntergekommene Ray Mahal, soll saniert und an jüngere, attraktivere Zeitgenossen vermietet werden. Das möchte das Quartett natürlich mit allen Mitteln verhindern. Und schon sind die schlitzohrigen Gauner in ihrem Element. Wen stört es da schon, dass man einen Toten aus dem städtischen Leichenhaus "borgen" muss und ein paranoider Drogenboss in die kleine Privatfehde hineingezogen wird. COPYRIGHT: Die Lizenz zur Veröffentlichung des Filmes auf Youtube wurde erworben von: Koch Media GmbH. .................................................................. LUST AUF MEHR FILME? On the Inside: http://bit.ly/1foh3kJ HD-Kino: http://bit.ly/1hdR7Ym Actionfilme: http://bit.ly/1fJdA0b Komödien: http://bit.ly/1huGe96 Horrorfilme: http://bit.ly/1huGeWI Thriller: http://bit.ly/1gWMLL3 Alle Playlists: http://bit.ly/1hXRU0z ..................................................................'
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
