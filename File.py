class File:
    
    def __init__(self):
        """Initialise une file vide."""
        self._items = [] 

    def est_vide(self):
        """Vérifie si une file est vide."""
        return not self._items

    def enfiler(self, element):
        """Ajouter l'élément dans la file (dernier élément)."""
        self._items.append(element)

    def defiler(self):
        """Retirer le premier élément de la file si elle n'est pas vide."""
        if self.est_vide():
            raise IndexError("Défiler d'une file vide")
        return self._items.pop(0)