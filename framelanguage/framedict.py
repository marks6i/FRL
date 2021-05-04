from framelanguage.frame import Frame
from framelanguage.slot  import Slot 

class FrameDict():

    def __init__(self, name, data=()):
        self.name = name
        self.frames = {}
        self.frames.update(data)


    def __repr__(self):
        return f"""{type(self).__name__}("{self.name}",{self.frames})"""


    def set(self, frame, slot, facet, value):
        aFrame = self.frames[frame]
        if not aFrame:
            self.frames[frame] = Frame(frame, { Slot(slot, { facet: value })})
            return self
        aFrame.set(slot, facet, value)
        return self


    def setValue(self, frame, slot, value):
        return self.set(frame, slot, '__value__', value)


    def setAKO(self, frame, slot, value):
        return self.set(frame, slot, '__AKO__', value)


    def get(self, frame, slot, facet):
        if not frame in self.frames:
            return
        return self.frames[frame].get(slot, facet)


    def getValue(self, frame, slot):
        return self.get(frame, slot, '__value__')


    def getAKO(self, frame, slot):
        return self.get(frame, slot, '__AKO__')


    def delete(self, frame, slot = None, facet = None):
        if not frame in self.frames:
            return
        if not slot:
            return self.frames.pop(frame, None)
        return self.frames[frame].delete(slot, facet)


    def to_dict(self):
        return { 'name': self.name, 'frames': { k: v.to_dict() for k,v in self.frames } }


    @classmethod
    def from_dict(cls, aDict):
        return FrameDict(aDict['name'], aDict['frames'])
