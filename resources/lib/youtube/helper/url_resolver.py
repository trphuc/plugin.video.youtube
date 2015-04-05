import urlparse

__author__ = 'bromix'

import resources.lib.kodion.simple_requests as requests


class AbstractResolver(object):
    def __init__(self):
        pass

    def supports_url(self, url, url_components):
        raise NotImplementedError()

    def resolve(self, url, url_components):
        raise NotImplementedError()

    pass


class SkipResolver(AbstractResolver):
    def __init__(self):
        self._skip_domains = [
            # Google
            'www.google.com',
            'www.play.google.com',
            # Apple
            'www.itunes.apple.com',
            # microsoft
            'www.apps.microsoft.com',
            'www.windowsphone.com',
            # other
            'www.amazon.de',
            'www.amazon.com',
            'www.amazon.co.uk',
            'www.facebook.com',
            'www.twitch.tv',
            'www.twitter.com',
            'www.instagram.com'
        ]
        pass

    def supports_url(self, url, url_components):
        return url_components.hostname.lower() in self._skip_domains or 'www.' + url_components.hostname.lower() in self._skip_domains

    def resolve(self, url, url_components):
        return url

    pass


class YouTubeResolver(AbstractResolver):
    def __init__(self):
        AbstractResolver.__init__(self)
        pass

    def supports_url(self, url, url_components):
        if url_components.hostname == 'www.youtube.com' or url_components.hostname == 'youtube.com':
            if url_components.path.lower() in ['/redirect', '/watch', '/playlist']:#, '/user']:
                return True
            pass

        return False

    def resolve(self, url, url_components):
        if url_components.path.lower() == '/redirect':
            params = dict(urlparse.parse_qsl(url_components.query))
            return params['q']

        return url

    pass


class CommonResolver(AbstractResolver):
    def __init__(self):
        AbstractResolver.__init__(self)
        pass

    def supports_url(self, url, url_components):
        return True

    def resolve(self, url, url_components):
        def _loop(_url, tries=5):
            if tries == 0:
                return _url

            response = requests.head(_url, allow_redirects=False)
            if response.status_code == 304:
                return url

            if response.status_code in [301, 302, 303]:
                headers = response.headers
                location = headers.get('location', '')

                # some server return 301 for HEAD requests
                # we just compare the new location - if it's equal we can return the url
                if location == _url or location + '/' == _url or location == _url + '/':
                    return _url

                if location:
                    return _loop(location, tries=tries - 1)

                # just to be sure ;)
                location = headers.get('Location', '')
                if location:
                    return _loop(location, tries=tries - 1)
                pass

            return _url

        resolved_url = _loop(url)

        return resolved_url

    pass


class UrlResolver(object):
    def __init__(self):
        self._cache = {}
        self._resolver = [
            YouTubeResolver(),
            SkipResolver(),
            CommonResolver()
        ]
        pass

    def resolve(self, url):
        # first test the simple cache
        resolved_url = self._cache.get(url, '')
        if resolved_url:
            return resolved_url

        # try one of the resolver
        url_components = urlparse.urlparse(url)
        for resolver in self._resolver:
            if resolver.supports_url(url, url_components):
                resolved_url = resolver.resolve(url, url_components)
                self._cache[url] = resolved_url
                return resolved_url
            pass

        # nothing to do
        self._cache[url] = url
        return url

    pass
