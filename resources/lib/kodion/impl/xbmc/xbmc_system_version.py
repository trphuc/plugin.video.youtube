__author__ = 'bromix'

import xbmc
import re
from ..abstract_system_version import AbstractSystemVersion


class XbmcSystemVersion(AbstractSystemVersion):
    def __init__(self):
        major = 0
        minor = 0
        try:
            self._version = tuple(map(int, (xbmc.__version__.split("."))))
        except:
            self._version = (1, 4)  # Frodo
            pass

        self._name = 'Unknown XBMC System'
        if self._version >= (1, 4) or self._version == (2, 0):
            self._name = 'Frodo'
            pass
        if self._version > (2, 0):
            self._name = 'Gotham'
            pass
        if self._version > (2, 14):
            self._name = 'Helix'
            pass
        pass

    pass