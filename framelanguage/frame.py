from collections.abc import MutableMapping

class Frame(MutableMapping):

    def __init__(self, name, data=()):
        self.name = name
        self.slots = {}
        self.update(data)

    def __getitem__(self, slot):
        if not slot in self.slots:
            return
        aSlot = self.slots[slot]
        if   '__value__' in aSlot:
            return aSlot['__value__']
        elif '_default__' in aSlot:
            return aSlot['__default__']
        return self.runValueDemon(slot)

    def __delitem__(self, slot):
        del self.slots[slot]

    def __setitem__(self, slot, facets):
        self.slots[slot] = facets

    def __iter__(self):
        return iter(self.slots)

    def __len__(self):
        return len(self.slots)

    def __repr__(self):
        return f"""{type(self).__name__}("{self.name}",{self.slots})"""

    def runValueDemon(self, slot):
        if not slot in self.slots:
            return
        aSlot = self.slots[slot]
        if '__ifNeeded__' in aSlot:
            block = aSlot['__ifNeeded__']
            return eval(block, {'frame': self, 'slot': self[slot]})
        return