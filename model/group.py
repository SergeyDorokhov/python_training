from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, comment=None, id=None):
        self.name = name
        self.header = header
        self.comment = comment
        self.id = id

    def __repr__(self):
        return "%s: %s, %s, %s" % (self.id, self.name, self.header, self.comment)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize
