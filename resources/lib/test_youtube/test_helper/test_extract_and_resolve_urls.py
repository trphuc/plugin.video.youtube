#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__ = 'bromix'

from resources.lib.youtube.helper import extract_urls, resolve_url

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
        for url in urls:
            res_urls.append(resolve_url(url))
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
        for url in urls:
            res_urls.append(resolve_url(url))
            pass
        pass
    pass
