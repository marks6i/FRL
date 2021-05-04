from framelanguage.slot import Slot

class Frame():

    def __init__(self, name, data=()):
        self.name = name
        self.slots = {}
        self.slots.update(data)


    def __repr__(self):
        return f"""{type(self).__name__}("{self.name}",{self.slots})"""


    def setName(self, name):
        self.name = name
        return self


    def set(self, slot, facet, value):
        if not slot in self.slots:
            self.slots[slot] = Slot(slot, { facet: value })
            return self
        aSlot = self.slots[slot]
        aSlot[facet] = value
        return self


    def get(self, slot, facet):
        if not slot in self.slots:
            return
        aSlot = self.slots[slot]
        return aSlot[facet]


    def delete(self, slot, facet = None):
        if not slot in self.slots:
            return
        if not facet:
            return self.slots.pop(slot, None)
        return self.slots[slot].pop(facet, None)


    def runValueDemon(self, slot):
        if not slot in self.slots:
            return
        aSlot = self.slots[slot]
        if '__ifNeeded__' in aSlot:
            block = aSlot['__ifNeeded__']
            return eval(block, {'frame': self, 'slot': aSlot})
        return


    def to_dict(self):
        return { 'name': self.name, 'slots': { k: v.to_dict() for k,v in self.slots } }


    @classmethod
    def from_dict(cls, aDict):
        return Frame(aDict['name'], aDict['slots'])
