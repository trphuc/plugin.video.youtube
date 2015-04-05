#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__ = 'bromix'

from resources.lib.youtube.helper import extract_urls
import unittest


class TestUrlExtract(unittest.TestCase):
    def test_description_1(self):
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
        self.assertEquals(7, len(urls))
        pass

    def test_description_2(self):
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
        urls = extract_urls(description)
        self.assertEquals(13, len(urls))
        pass

    def test_description_3(self):
        description = 'Alle FSK16 und 18 Filme findest du auf http://www.netzkino.de und der gratis Netzkino App! Netzkino Android App - https://play.google.com/store/apps/details?id=de.netzkino.android.ics Netzkino iOS App - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 .................................................................. SECOND CHANCE - ALLES WIRD GUT Die Mafia-Komödie mit Burt Reynolds (Boogie Nights) von 2000. Mit: Richard Dreyfuss, Dan Hedaya | Regie: Michael Dinner FSK: Freigegeben ab 12 Jahren .................................................................. NETZKINO ABONNIEREN: https://www.youtube.com/user/Netzkino?sub_confirmation=1 .................................................................. NETZKINO ANDROID APP herunterladen - https://play.google.com/store/apps/details?id=de.netzkino.android.ics NETZKINO iOS APP herunterladen - https://itunes.apple.com/ch/app/netzkino/id560901396?mt=8 NETZKINO WINDOWS 8 APP herunterladen - http://apps.microsoft.com/windows/de-de/app/netzkino/fc8ac95f-b14e-44ef-a148-9a4c7bec7919 NETZKINO WINDOWS PHONE APP herunterladen - http://www.windowsphone.com/de-de/store/app/netzkino/3734d2e8-c646-472d-94cb-fc021505867c NETZKINO AMAZON APP herunterladen - http://www.amazon.de/Netzkino-Services-GmbH/dp/B00MR1YQM8 FACEBOOK - https://www.facebook.com/netzkino. TWITTER - https://twitter.com/netzkino GOOGLE+ - https://plus.google.com/+netzkino NETZKINO.DE - http://www.netzkino.de .................................................................. INHALTSANGABE: Sie sind alt. Sie sind in Rente. Aber sie haben nichts verlernt. Die Ex-Mafiosi Bobby, Joey, Mike und Tony haben sich im sonnigen South Beach, Miami, zur Ruhe gesetzt. Doch die vier Senioren müssen noch einmal in ihre Trickkiste greifen: Ihr Altersruhesitz, das heruntergekommene Ray Mahal, soll saniert und an jüngere, attraktivere Zeitgenossen vermietet werden. Das möchte das Quartett natürlich mit allen Mitteln verhindern. Und schon sind die schlitzohrigen Gauner in ihrem Element. Wen stört es da schon, dass man einen Toten aus dem städtischen Leichenhaus "borgen" muss und ein paranoider Drogenboss in die kleine Privatfehde hineingezogen wird. COPYRIGHT: Die Lizenz zur Veröffentlichung des Filmes auf Youtube wurde erworben von: Koch Media GmbH. .................................................................. LUST AUF MEHR FILME? On the Inside: http://bit.ly/1foh3kJ HD-Kino: http://bit.ly/1hdR7Ym Actionfilme: http://bit.ly/1fJdA0b Komödien: http://bit.ly/1huGe96 Horrorfilme: http://bit.ly/1huGeWI Thriller: http://bit.ly/1gWMLL3 Alle Playlists: http://bit.ly/1hXRU0z ..................................................................'
        urls = extract_urls(description)
        self.assertEquals(20, len(urls))
        pass

    pass
