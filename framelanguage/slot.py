from collections.abc import MutableMapping

class Slot(MutableMapping):

    def __init__(self, name, data=()):
        self.name = name
        self.facets = {}
        self.update(data)


    def __repr__(self):
        return f"{type(self).__name__}('{self.name}',{self.facets})"


    def __getitem__(self, facet):
        return self.facets[facet]


    def __delitem__(self, facet):
        del self.facets[facet]


    def __setitem__(self, facet, value):
        self.facets[facet] = value


    def __iter__(self):
        return iter(self.facets)


    def __len__(self):
        return len(self.facets)


    def to_dict(self):
        return { 'name': self.name, 'facets': self.facets }


    @classmethod
    def from_dict(cls, aDict):
        return Slot(aDict['name'], aDict['facets'])
