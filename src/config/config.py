__config = None
class Config(object):
    def __init__(self):
        self._debug = False

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value

def setConfig(config: Config):
    global __config
    __config = config

def getConfig() -> Config:
    return __config