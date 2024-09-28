class Config(object):
    def __init__(self):
        self._debug = False

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value