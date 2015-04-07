#!/usr/bin/env python
# -*- coding: utf-8 -*
from resources.lib import kodion

__author__ = 'bromix'

from resources.lib.youtube.helper import extract_urls, UrlResolver

import unittest


class TestUrlExtract(unittest.TestCase):
    def test_urls(self):
        urls = [
            ('https://www.youtube.com/redirect?q=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D9DKZbZyW2-g%26list%3DPL3tRBEVW0hiAOf_drlpS1hqZjJknW88cB%26index%3D1&redir_token=IBH7ovJdGv031f2JRlnYAKfq0m98MTQyODE1NjI2MEAxNDI4MDY5ODYw', 'http://www.youtube.com/watch?v=9DKZbZyW2-g&list=PL3tRBEVW0hiAOf_drlpS1hqZjJknW88cB&index=1'),
            ('http://smo.sh/SubscribeSmoshGames', 'https://www.youtube.com/channel/UCJ2ZDzMRgSrxmwphstrm8Ww?sub_confirmation=1'),
            ('https://youtu.be/GdhfwW5zHEY', 'https://www.youtube.com/watch?v=GdhfwW5zHEY&feature=youtu.be'),
            ('http://ow.ly/LcFu4', 'http://www.heise.de/'),
            ('http://goo.gl/CRiy4L', 'http://www.shortnews.de')
        ]

        context = kodion.Context()
        resolver = UrlResolver(context)
        for url in urls:
            resolved_url = resolver.resolve(url[0])
            self.assertEquals(resolved_url, url[1])
            pass
        pass

    def test_resolve_urls_1(self):
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

        res_urls = []
        urls = extract_urls(description)
        context = kodion.Context()
        resolver = UrlResolver(context)
        for url in urls:
            res_urls.append(resolver.resolve(url))
            pass
        pass

    def test_resolve_urls_2(self):
        description = (
            'An wild and bizarre adventure through the unreal and the unforgiving... HURRAY!!\n'
            'MORE Scary Games ► https://www.youtube.com/playlist?list=PL3tRBEVW0hiBSFOFhTC5wt75P2BES0rAo\n'
            'Exmortis ► https://youtu.be/GdhfwW5zHEY\n'
            'The House ► https://youtu.be/eQxgWut4T4c\n'
            'Subscribe Today! ► http://bit.ly/Markiplier\n'
            '\n'
            'Play the Game ► http://www.newgrounds.com/portal/view/654784\n'
            '\n'
            'You Might Also Like ▼\n'
            'Markiplier Highlights - https://www.youtube.com/redirect?q=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D9DKZbZyW2-g%26list%3DPL3tRBEVW0hiAOf_drlpS1hqZjJknW88cB%26index%3D1&redir_token=IBH7ovJdGv031f2JRlnYAKfq0m98MTQyODE1NjI2MEAxNDI4MDY5ODYw\n'
            'Horror Compilations - https://www.youtube.com/redirect?q=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dp03A7QTBuhg%26list%3DPL58D8AC6A97A69F45%26index%3D1&redir_token=IBH7ovJdGv031f2JRlnYAKfq0m98MTQyODE1NjI2MEAxNDI4MDY5ODYw\n'
            'Happy Wheels - https://www.youtube.com/redirect?q=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DveIB_RI8yMY%26list%3DPL3tRBEVW0hiBMoF9ihuu-x_aQVXvFYHIH%26index%3D2&redir_token=IBH7ovJdGv031f2JRlnYAKfq0m98MTQyODE1NjI2MEAxNDI4MDY5ODYw'
            '\n'
            'Follow my Instagram ► http://instagram.com/markipliergram\n'
            'Follow me on Twitter ► https://twitter.com/markiplier\n'
            'Like me on Facebook ► https://www.facebook.com/markiplier\n'
            '\n'
            'T-Shirts ► http://1shirt.com/collections/markiplier/products/markiplier-warfstache\''
            'Livestreams ► http://www.twitch.tv/markiplier'
        )

        res_urls = []
        urls = extract_urls(description)
        context = kodion.Context()
        resolver = UrlResolver(context)
        for url in urls:
            res_urls.append(resolver.resolve(url))
            pass
        pass

    def test_resolve_urls_3(self):
        description = '(http://www.youtubAlle FSK16 und 18 Filme findest du auf http://www.netzkino.de und der gratis Netzkino App! Netzkino Android App - https://play.google.com/store/apps/details?id=de.netzkino.android.ics Netzkino iOS App - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 .................................................................. KIFFERWAHN Völlig abgedrehte Musical-Komödie mit Kristen Bell von 2005. Mit: Christian Campbell, Neve Campbell | Regie: Andy Fickman FSK: Freigegeben ab 12 Jahren .................................................................. NETZKINO ABONNIEREN: https://www.youtube.com/user/Netzkino?sub_confirmation=1 .................................................................. NETZKINO ANDROID APP herunterladen - https://play.google.com/store/apps/details?id=de.netzkino.android.ics NETZKINO iOS APP herunterladen - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 NETZKINO WINDOWS 8 APP herunterladen - http://apps.microsoft.com/windows/de-de/app/netzkino/fc8ac95f-b14e-44ef-a148-9a4c7bec7919 NETZKINO WINDOWS PHONE APP herunterladen - http://www.windowsphone.com/de-de/store/app/netzkino/3734d2e8-c646-472d-94cb-fc021505867c NETZKINO AMAZON APP herunterladen - http://www.amazon.de/Netzkino-Services-GmbH/dp/B00MR1YQM8 FACEBOOK - https://www.facebook.com/netzkino. TWITTER - https://twitter.com/netzkino GOOGLE+ - https://plus.google.com/+netzkino NETZKINO.DE - http://www.netzkino.de .................................................................. INHALTSANGABE: Jimmy und Mary, das amerikanische Vorzeige-Teenagerpaar schlechthin, bereiten sich auf eine Englisch-Prüfung an der High-School und ein erfülltes Familienleben vor. Doch Jimmy gerät in die Fänge des Marihuana-Dealers und Jazz-Freaks Jack. Ein Zug an der Haschischzigarette und der saubere Jimmy verwandelt sich in ein unmoralisches Monster, das nur noch auf Sex, Anarchie und dem nächsten Joint lechtzt. Widerwärtige Ausschweifungen, Tote, Irrsinn und schwerste Rechtsverletzungen sind die Folge des Stoffes, der Amerika zu vernichten droht. Jimmy und seine neuen Freunde stellen im Drogenrausch die furchtbarsten Dinge an, ständig begleitet von infernalischer Musik. Das schonungslose Ende naht, als die sonst so brave Mary im Rausch des Giftes ihre Qualitäten als Domina entdeckt. COPYRIGHT: Die Lizenz zur Veröffentlichung des Filmes auf Youtube wurde erworben von: Koch Media GmbH. .................................................................. LUST AUF MEHR FILME? Paradise Trouble: http://bit.ly/1m7iawz Neu bei Netzkino: http://bit.ly/PcVRYy HD-Kino: http://bit.ly/1hdR7Ym Actionfilme: http://bit.ly/1fJdA0b Komödien: http://bit.ly/1huGe96 Horrorfilme: http://bit.ly/1huGeWI Thriller: http://bit.ly/1gWMLL3 Alle Playlists: http://bit.ly/1hXRU0z ..................................................................'
        urls = extract_urls(description)
        context = kodion.Context()
        resolver = UrlResolver(context)
        res_urls = []
        for url in urls:
            res_urls.append(resolver.resolve(url))
            pass
        pass
    pass
