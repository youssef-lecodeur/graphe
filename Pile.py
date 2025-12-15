class Pile:
    
    def __init__(self):
        self._items = [] 

    def est_vide(self):
        return not self._items

    def empiler(self, element):
        self._items.append(element)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Dépiler d'une pile vide")
        return self._items.pop()