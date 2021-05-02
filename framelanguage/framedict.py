from collections.abc import MutableMapping

class FrameDict(MutableMapping):

    def __init__(self, name, data=()):
        self.name = name
        self.frames = {}
        self.update(data)

    def __getitem__(self, frame):
        if not frame in self.frames:
            return
        return self.frames[frame]

    def __delitem__(self, frame):
        del self.frames[frame]

    def __setitem__(self, frame, slots):
        self.frames[frame] = slots

    def __iter__(self):
        return iter(self.frames)

    def __len__(self):
        return len(self.frames)

    def __repr__(self):
        return f"""{type(self).__name__}("{self.name}",{self.frames})"""

    def setAKO(self, frame, ancestor):
        pass

    def getAKO(self, frame):
        pass